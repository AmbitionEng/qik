"""Core hashing functions."""

from __future__ import annotations

import collections
import re
import subprocess
from typing import TYPE_CHECKING

import xxhash

import qik.conf
import qik.errors
import qik.func
import qik.shell

if TYPE_CHECKING:
    import qik.dep as run_deps
    import qik.venv


def _hexdigest(data: str | bytes) -> str:
    """Hash with xxh128, encoding str first (xxhash >= 4.0 rejects str input)."""
    if isinstance(data, str):
        data = data.encode()
    return xxhash.xxh128_hexdigest(data)


def _run_with_stdin(cmd: list[str], stdin_data: str) -> list[str]:
    """Run a command with data piped via stdin, avoiding ARG_MAX limits."""
    result = subprocess.run(
        cmd,
        input=stdin_data,
        text=True,
        capture_output=True,
        check=True,
        cwd=qik.conf.root(),
    )
    return [line for line in result.stdout.strip().split("\n") if line]


def globs(*vals: run_deps.Glob | str) -> str:
    """Compute a hash string of glob patterns.

    Use git ls-files, tracking both added and modified file hashes.

    If local ._qik/artifacts/ exists, we'll manually hash these.
    """
    if not vals:
        return ""

    globs = {f"{glob}" for glob in vals}

    priv_artifact_patterns = sorted(
        f"'{glob[16:]}'" for glob in globs if glob.startswith("._qik/artifacts/")
    )
    priv_artifact_hash = ""
    if priv_artifact_patterns:
        priv_artifact_hash = qik.shell.exec(
            f"git -C ._qik/artifacts hash-object {' '.join(priv_artifact_patterns)}",
            check=True,
        ).stdout

    repo_patterns = sorted(glob for glob in globs if not glob.startswith("._qik/artifacts/"))
    repo_hash = ""
    if repo_patterns:
        # Pipe patterns via stdin to xargs to avoid ARG_MAX limits
        patterns_input = "\n".join(repo_patterns)
        git_ls_lines = _run_with_stdin(
            ["xargs", "git", "ls-files", "-cms"],
            patterns_input,
        )
        git_ls_lines_split = [
            (path, sha)
            for _, sha, _, path in (re.split(r"\s+", line, maxsplit=3) for line in git_ls_lines)
        ]
        hashes = dict(git_ls_lines_split)

        # Files that are modified appear twice. Manually compute their hashes
        path_counts = collections.Counter(line[0] for line in git_ls_lines_split)
        modified = [path for path, count in path_counts.items() if count > 1]
        if modified:
            modified_paths_str = "\n".join(modified)
            try:
                modified_hashes_lines = _run_with_stdin(
                    ["xargs", "git", "hash-object"],
                    modified_paths_str,
                )
            except subprocess.CalledProcessError:
                # If there are issues with the first command, it likely means a file does
                # not exist. Do the suboptimal strategy here, hashing individual files
                # while printing zeroes for files that no longer exist.
                modified_hashes_lines = []
                for path in modified:
                    try:
                        result = subprocess.run(
                            ["git", "hash-object", path],
                            text=True,
                            capture_output=True,
                            check=True,
                            cwd=qik.conf.root(),
                        )
                        modified_hashes_lines.append(result.stdout.strip())
                    except subprocess.CalledProcessError:
                        modified_hashes_lines.append("0000000000000000000000000000000000000000")

            for i, name in enumerate(modified):
                # TODO: Occasionally we can get a list index out of range error here. It seems
                # to be due to a race condition. Re-raise it for now with more context in hopes
                # of better debugging it.
                try:
                    hashes[name] = modified_hashes_lines[i]
                except IndexError as e:
                    raise RuntimeError(f"Unexpected error when computing hash. {modified}") from e

        repo_hash = "".join(f"{name}{hash}" for name, hash in sorted(hashes.items()))

    return _hexdigest(priv_artifact_hash + repo_hash)


def pydists(*vals: str, venv: qik.venv.Venv) -> str:
    return _hexdigest("".join(f"{pydist}{venv.version(pydist)}" for pydist in sorted(vals)))


def strs(*vals: str) -> str:
    return _hexdigest("".join(sorted(vals)))


def val(input: str | bytes) -> str:
    return _hexdigest(input)

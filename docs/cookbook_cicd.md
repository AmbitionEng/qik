# Continuous Integration and Delivery

Qik can be used in a number of ways to dramatically increase CI/CD performance. Here we cover various patterns to use with new or existing projects.

!!! tip

    The core `qik` installation is the only requirement needed in CI/CD.

## Ensuring that Repo-Cached Commands are Successful

When using the `repo` cache, we can quickly verify that all commands are successful with:

```bash
qik --cache repo --cache-status cold --fail --ls
```

Above, we're doing the following:

- Filtering commands by `--cache` of `repo`
- Filtering for any `cold` commands
- Failing if any exist
- Printing the commands that aren't cached

If all commands are cached, we can run them all with:

```bash
qik --cache repo
```

The second step ensures that any cached failures are caught. By default, only successful runs are cached, but this may have been overridden with `--cache-when`.

With these commamnds, you now have a fast way to ensure your repo cache is in sync.

## Using a Remote Cache

### Basics

If repo-based caching isn't acceptable or you have architecture-specific commands, use a [remote cache](caching.md#remote). Just remember to configure `artifacts` for your commands. For example, let's run [pytest](https://docs.pytest.org/en/stable/) over modules and collect coverage reports:

```toml
[commands.pytest]
exec = "pytest --cov {module.dir} --cov-report xml:{module.name}-coverage.xml"
deps = [{type = "pygraph", pyimport = "{module.pyimport}"}]
artifacts = ["{module.name}-coverage.xml"]
```

Run `qik pytest --cache my_remote_cache_name`. When the cache is warm, the output will be replayed and the coverage artifacts will be restored.

### Configuration

We recommend making a CI profile to specify the default cache:

```toml
[ctx.ci.qik]
cache = "my_remote_cache_name"
```

Use either `-p ci` or set `QIK__PROFILE=ci` in your environment to use the default CI configuration. If using the [S3 cache](plugin_s3.md), remember to set AWS authentication environment variables.

## Isolated Execution

If commands have other [command dependencies](commands.md#command), these will also be selected even if trying to run a single command with `qik <command_name>`. This is normally harmless since upstream commands are usually cached, however it can be undesirable if using a slower remote cache.

To bypass this, use `--isolated` when running the command. Remember, using [import graph dependencies](plugin_pygraph.md) will automatically insert dependent commands, so be sure to either validate the repo cache or run upstream commands elsewhere in your CI/CD flow.

## Dynamic CI/CD Config Generation

Some CI/CD services such as [CircleCI](https://circleci.com) offer the ability to [dynamically generate configuration](https://circleci.com/docs/dynamic-config/). You can leverage this pattern as follows:

- In the initial step, run `qik --cache-status warm` to run all warm commands. All artifacts will be available in your repository to store as CI/CD artifacts.
- Then iterate over `qik --cache-status cold --ls` to configure the remaining jobs for execution.

Keep the following in mind:

- Any commands that have set `cache_when = "finished"` will cache failures, causing the first command to fail.
- Any parametrized commands from `--ls` will be in the format of `{command}@{module}`.

## Running Since a Base Branch

Use `--since <base branch>` to select commands that need to be re-executed since a base branch (e.g. in a pull request). Remember to keep the following in mind:

- If you rely on artifacts such as coverage reports on every CI run, these may not be produced if you don't run those commands.
- Qik is still in beta. It's good to occasionally break the whole cache by [adding a const dependency](commands.md#const) as a [base dependency](commands.md#base).

!!! warning

    We recommend always running every command and leveraging a cache, but using `--since` can help with very large monorepos where this isn't possible.

## Recap

There are several tools at your disposal to optimize your CI/CD experience. By leveraging these, you can:

- Keep your platform-agnostic commands cached in the repo, avoiding the need to run these commands with your CI/CD provider.
- Use a shared remote cache to avoid re-running the same work.
- Store artifacts of cached runs in the artifact store of your CI/CD provider.
- Dynamically generate CI/CD config by listing commands based on their cache type.

We recommend running `qik --cache repo --watch` locally to always keep the repo cache up to date.

Qik is still in beta. Open a [discussion](https://github.com/AmbitionEng/qik/discussions) if you have other ideas or suggestions on how to improve the local development and CI/CD experience.

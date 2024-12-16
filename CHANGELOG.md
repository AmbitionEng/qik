# Changelog

## 0.2.2 (2024-12-15)

#### Changes

  - Drop support for Python 3.9, changed project ownership to `AmbitionEng` by [@wesleykendall](https://github.com/wesleykendall) in [#14](https://github.com/AmbitionEng/qik/pull/14).

## 0.2.1 (2024-10-26)

#### Feature

- Support earlier versions of git where `--format` was not an option of `git ls-files`.

## 0.2.0 (2024-10-13)

#### API Break

- Add qik *spaces* for isolated command execution.
- Create an extensible plugin system and three initial plugins: pygraph, UV, and S3.

Plus many more improvements. See [the blog post on spaces](https://qik.build/en/stable/blog/2024/10/12/introducing-spaces/) for more details.

## 0.1.6 (2024-08-20)

#### Trivial

  - Includes the ability to override missing module and distributions, along with much better error handling for individual failures in the runner. [Wesley Kendall, fe5d844]

## 0.1.5 (2024-08-19)

#### Trivial

  - Better error handling and references to docs on errors. [Wesley Kendall, 089c132]

## 0.1.4 (2024-08-16)

#### Trivial

  - Added basic test suite. [Wesley Kendall, 66a9d16]

## 0.1.3 (2024-08-14)

#### Trivial

  - Update blog post and other misc fixes. [Wesley Kendall, 5a300d6]

## 0.1.2 (2024-08-13)

#### Trivial

  - Fix README link to blog post [Wesley Kendall, 0b930b5]

## 0.1.1 (2024-08-12)

#### Trivial

  - Force a re-build of the docs to remove ads. [Wesley Kendall, 0274fde]

## 0.1.0 (2024-08-12)

#### Feature

  - Qik beta release. [Wesley Kendall, d56e7ab]

    The qik beta release includes the initial command runner and docs.
    See https://qik.build for an overview of functionality.

## 0.0.4 (2024-08-09)

#### Trivial

  - Misc doc additions [Wesley Kendall, 2736c18]

## 0.0.3 (2024-08-08)

#### Trivial

  - Generate .gitattributes, fix module import watching, add verbosity levels. [Wesley Kendall, 67c7623]

## 0.0.2 (2024-08-05)

#### Trivial

  - Fix ReadTheDocs build. [Wesley Kendall, 51d835e]

## 0.0.1 (2024-08-05)

#### Trivial

  - The initial qik alpha release. [Wesley Kendall, 4d2d43b]

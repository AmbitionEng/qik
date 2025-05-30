---
hide:
  - navigation
---

# Roadmap

Qik has several large upcoming features. If you'd like to suggest other future direction or let us know what you think, [open a discussion here](https://github.com/AmbitionEng/qik/discussions). If you'd like to contribute any of these core changes, [contact Wes first](mailto:wesleykendall@gmail.com).

## Better Import Graph Control

#### Direct Import Dependency Specification &nbsp; :white_check_mark:<code>v0.2.0</code>

One must configure a module in the `qik.toml` modules list in order to use it as a module dependency. We plan to decouple this and allow people to directly express which module import dependencies.

#### Auto-Ignoring Missing Distributions &nbsp; :white_check_mark:<code>v0.1.6</code>

Some distributions in a project may be optional and not installed, causing the graph builder to fail. Currently one can [globally disable external distributions from the graph](plugin_pygraph.md#troubleshooting), however, we plan for better control over this.

#### Ignoring Specific Distributions &nbsp; :white_check_mark:<code>v0.1.6</code>

We intend to allow users to explicitly disable certain distributions from the graph.

<a id="ignoring-specific-patterns"></a>
#### Adding and Removing Import Links

Users must [manually import modules](plugin_pygraph.md) in a Python file if those imports are dynamic. We are planning to allow for more explicit control over this, along with removing imports from the graph. For example, one will be able to remove imports from their migration files.

## Better Virtual Environment (Venv) Support

#### Run Commands in Venvs &nbsp; :white_check_mark:<code>v0.2.0</code>

Qik requires an activated venv to run commands. We plan to remove this requirement.

#### Using Lock Files to Find Distribution Versions

Venvs must be installed to find a distribution version. We will enable lock files as a back-up source of truth, alleviating the need to install tools for repo-cached commands.

#### Multiple Venvs &nbsp; :white_check_mark:<code>v0.2.0</code>

We're adding support for running commands in multiple venvs

#### Building Venvs &nbsp; :white_check_mark:<code>v0.2.0</code>

We will support building virtual environments with various backends such as [pip-tools](https://github.com/jazzband/pip-tools), [poetry](https://python-poetry.org), and [uv](https://github.com/astral-sh/uv).

#### Venvs with Binaries

We also intend to support [Conda-enabled virtual environments](https://conda.io), enabling users to specify Python versions, install [Node](https://nodejs.org), and manage a plethora of other libraries and tools available via [conda forge](https://conda-forge.org).

## Better Command Selection and Running

<a id="spaces"></a>

#### Spaces &nbsp; :white_check_mark:<code>v0.2.0</code>

We are planning for qik *spaces*, the ability to isolate areas of your monorepo and apply default configuration for the command runner.

With this construct, we hope to:

- Enable import linting commands to keep areas of your monorepo isolated.
- Enable other types of plugins, such as ones that generate Dockerfiles from your space.

#### Tags &nbsp; :white_check_mark:<code>v0.2.4</code>

Users will be able to tag their commands, making it easier to select and filter them.

#### Meta Commands

Qik will support *meta* commands, which have a separate syntax and function. For example, the `:graph` command will enable inspection of the import graph. The `:cache` meta command will aid in clearing and viewing caches.

#### Daemon Commands

Commands that never return (e.g. servers) will be supported as first-class citizens in the qik runner for an even more powerful local develop experience and plugin ecosystem.

#### Tab Completion

Qik commands will have tab-completion support in the shell.

#### Textual Admin

Running many commands can be cumbersome, especially if you want to see interactive output. We are planning to create a [textual](https://textual.textualize.io) terminal UI for an even better experience of watching and running many commands.

#### Git Hooks

We are planning the ability to better link into [git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks), such as running commands before committing or pushing. 

## Plugins

#### A More Extensible Plugin System &nbsp; :white_check_mark:<code>v0.2.0</code>

Our plugin system is not very extensible at the moment. We will be allowing for third party plugins to better define custom caches, custom commands, and much more.

#### More Remote Caches

We plan to support more remote caches. We'll likely implement the primary object storage systems at first such as [Google Cloud Storage](https://cloud.google.com/storage).

#### Importing Linting &nbsp; :white_check_mark:<code>v0.2.0</code>

We're planning for an import linting plugin with [spaces](#spaces).

#### Dockerfile Generation

We're planning a plugin to generate Dockerfiles based on [spaces](#spaces) and commands.

#### Dot Env Files &nbsp; :white_check_mark:<code>v0.2.0</code>

We plan to support [dotenv](https://www.npmjs.com/package/dotenv) files being attached to [qik contexts](context.md) or [spaces](#spaces), making it easier to associate environment variables with commands.

#### JavaScript Import Dependencies

We'd like to support JavaScript import dependencies. Qik's graph plugin serializes an import graph and translates it to glob patterns for each module. It's feasible to do the same approach for JavaScript projects. Ideally the import graph traversal is fast and written in a low-level language. Qik, for example, uses [grimp](https://grimp.readthedocs.io/en/stable/) to parse the Python import graph in [Rust](https://www.rust-lang.org).

## Suggestions?

[Open a discussion here](https://github.com/AmbitionEng/qik/discussions) if you have any thoughts or ideas about qik's roadmap.

# cipg
Playground for trying out CI configs, project hosting
platforms/applications and workflows.

- Codeberg: [babab/cipg](https://codeberg.org/babab/cipg)
- Github: [babab/cipg](https://github.com/babab/cipg)

## Index

<!-- vim-markdown-toc GFM -->

* [Project setup and management](#project-setup-and-management)
    * [Tools](#tools)
    * [Makefile](#makefile)
    * [Taskfile.dist.yml](#taskfiledistyml)

<!-- vim-markdown-toc -->


## Project setup and management

This project also acts as a means to create a generic template setup
for project management and development flow through `pyproject.toml`,
`Makefile` and/or `Taskfile` for python projects. In particular for
command line applications and scripts.

The actual python code part is just a tiny command line application with
unittests.


### Tools

There are between 10-20 different build/packaging
tools for Python projects. This setup is build around
[flit](https://flit.pypa.io/en/latest/rationale.html) for building
packages; [pipx](https://pypa.github.io/pipx/comparisons/)
for installing as a python module/script and
[pyinstaller](https://pyinstaller.org/en/stable/operating-mode.html) for
freezing / compiling a program into a single executable with Python and
libraries included.

The Makefile targets and Taskfile tasks are in sync and have identical
names and workings. You only need to use one program (make) or the other
(go-task).


### Makefile

This makefile is meant to aid in development flow as well as
document it. Regular users should follow the instructions on
installing cipg in the README.

To work on this project while keeping package dependencies isolated
from system packages, you can either use:

- `make pipx-develop` to have command(s) directly available in PATH
- `make develop` to keep the command(s) out your PATH (by default,
  but available after sourcing bin/activate).

The test target will install a link to the project code so that
the source and tests can be inspected for code coverage.

The test-pkg target will always build and install using the
wheel dist, even when this project is already installed with an
--editable flag. This is to minimize any issues that may arise
in the packaging process by including it in testing. This target
does not check for coverage.

----------------------------------------------------------------

*Run `make` without arguments or `make help` to show this help
information on the command line.*

<details><summary>Usage</summary>

``` console
HELP
 help         - show this help information
 release      - show manual release steps

BUILD AND TEST TARGETS (using venv at .virtualenv)
 test         - make develop and run tests through Coverage.py
 develop      - install into venv with 'pip install --editable .'
 exe          - build a single executable file with pyinstaller
 test-pkg     - install pkg and run checks/tests without coverage

PIPX TARGETS (using ~/.local/pipx/venvs/cipg)
 pipx-install - flit build and install with pipx install
 pipx-devel   - install with 'pipx install --editable .'
 pipx-remove  - same as pipx uninstall cipg

MISC TARGETS that are used as precursors in the targets above
 build | dist - flit build
 clean        - remove venv, build and dist directories
 get-pipx     - install pipx into user site-packages if not in PATH
 venv         - only make virtualenv and install build deps
 venv-install - install into venv with all dependencies/extras
```

</details>

### Taskfile.dist.yml

*For more info, see: https://github.com/go-task/task and/or
https://taskfile.dev*

----------------------------------------------------------------

This taskfile is meant to aid in development flow as well as
document it. Regular users should follow the instructions on
installing cipg in the README.

To work on this project while keeping package dependencies isolated
from system packages, you can either use:

- `task pipx-develop` to have command(s) directly available in PATH
- `task develop` to keep the command(s) out your PATH (by default,
  but available after sourcing bin/activate).

The test task will install a link to the project code so that
the source and tests can be inspected for code coverage.

The test-pkg task will always build and install using the
wheel dist, even when this project is already installed with an
--editable flag. This is to minimize any issues that may arise
in the packaging process by including it in testing. This task
does not check for coverage.

*Run `task` without arguments or `task help` to show this help
information on the command line. Because the name task is so generic,
it will sometimes be installed as `go-task` instead.*

<details><summary>Usage</summary>

``` console
HELP
 help         - show this help information
 release      - show manual release steps

BUILD AND TEST TASKS (using venv at .virtualenv)
 test         - make develop and run tests through Coverage.py
 develop      - install into venv with 'pip install --editable .'
 exe          - build a single executable file with pyinstaller
 test-pkg     - install pkg and run checks/tests without coverage

PIPX TASKS (using ~/.local/pipx/venvs/cipg)
 pipx-install - flit build and install with pipx install
 pipx-devel   - install with 'pipx install --editable .'
 pipx-remove  - same as pipx uninstall cipg

MISC TASKS that are used as precursors in the tasks above
 build | dist - flit build
 clean        - remove venv, build and dist directories
 get-pipx     - install pipx into user site-packages if not in PATH
 venv         - only make virtualenv and install build deps
 venv-install - install into venv with all dependencies/extras
```

</details>

# cipg
Playground for trying out CI configs, project hosting
platforms/applications and workflows.

- Codeberg: [babab/cipg](https://codeberg.org/babab/cipg)
- Github: [babab/cipg](https://github.com/babab/cipg)

## Make targets

Run `make` without arguments or `make help` to show help:

    # This makefile is meant to aid in development flow as well as
    # document it. Regular users should follow the instructions on
    # installing cipg in the README.
    #
    # To work on this project while keeping package dependencies isolated
    # from system packages, you can either use:
    #
    # - 'make pipx-develop' to have command(s) directly available in PATH
    # - 'make develop' to keep the command(s) out your PATH (by default,
    #   but available after sourcing bin/activate).
    #
    # The test target will always build and install using the wheel dist,
    # even when this project is already installed with an --editable flag.
    # This is to minimize any issues that may arrise in the packaging
    # process by including it in testing.
    #
    # HELP
    #  help         - show this help information
    #  release	- show manual release steps
    #
    # BUILD AND TEST TARGETS (using venv at .virtualenv)
    #  test         - build and install; check style and run unit tests
    #  develop      - install into venv with 'pip install --editable .'
    #  exe          - build a single executable file with pyinstaller'
    #
    # PIPX TARGETS (using ~/.local/pipx/venvs/cipg)
    #  pipx-install - flit build and install with pipx install
    #  pipx-devel   - install with 'pipx install --editable .'
    #  pipx-remove  - same as pipx uninstall cipg
    #
    # MISC TARGETS that are primarily precursors to the targets above
    #  build | dist - flit build
    #  clean        - remove venv, build and dist directories
    #  get-pipx     - install pipx into user site-packages if not in PATH
    #  venv         - only make virtualenv and install build deps
    #  venv-install - install into venv with all dependencies/extras

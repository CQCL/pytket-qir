# pytket-TODOEXTNAME

[![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://tketusers.slack.com/join/shared_invite/zt-18qmsamj9-UqQFVdkRzxnXCcKtcarLRA#)
[![Stack Exchange](https://img.shields.io/badge/StackExchange-%23ffffff.svg?style=for-the-badge&logo=StackExchange)](https://quantumcomputing.stackexchange.com/tags/pytket)

[Pytket](https://tket.quantinuum.com/api-docs/index.html) is a python module for interfacing
with CQC tket, a set of quantum programming tools.

`pytket-TODOEXTNAME` is an extension to `pytket` that allows `pytket` circuits to be
executed on .

Some useful links:

- [API Documentation](https://tket.quantinuum.com/extensions/pytket-TODOEXTNAME/)

## Getting started

`pytket-TODOEXTNAME` is compatible with Python versions 3.10 to 3.13 on Linux, MacOS
and Windows. To install, run:

```shell
pip install pytket-TODOEXTNAME
```

This will install `pytket` if it isn't already installed, and add new classes
and methods into the `pytket.extensions` namespace.

## Bugs and feature requests

Please file bugs and feature requests on the Github
[issue tracker](https://github.com/CQCL/pytket-TODOEXTNAME/issues).

## Development

To install an extension in editable mode, simply change to its subdirectory
within the `modules` directory, and run:

```shell
pip install -e .
```

## Contributing

Pull requests are welcome. To make a PR, first fork the repo, make your proposed
changes on the `main` branch, and open a PR from your fork. If it passes
tests and is accepted after review, it will be merged in.

### Code style

#### Formatting

All code should be formatted using
[ruff](https://docs.astral.sh/ruff/formatter/), with default options. This is
checked on the CI.

#### Type annotation

On the CI, [mypy](https://mypy.readthedocs.io/en/stable/) is used as a static
type checker and all submissions must pass its checks. You should therefore run
`mypy` locally on any changed files before submitting a PR. Because of the way
extension modules embed themselves into the `pytket` namespace this is a little
complicated, but it should be sufficient to run the script `./mypy-check`
(passing as a single argument the root directory of the module to test).

#### Linting

We use [ruff](https://github.com/astral-sh/ruff) on the CI to check compliance with a set of style requirements (listed in `ruff.toml`).
You should run `ruff` over any changed files before submitting a PR, to catch any issues.

An easy way to meet all formatting and linting requirements is to issue `pre-commit run --all-files`.

### Tests

To run the tests for a module:

1. `cd` into that module's `tests` directory;
2. ensure you have installed `pytest`, `hypothesis`, and any modules listed in
   the `test-requirements.txt` file (all via `pip`);
3. run `pytest`.

When adding a new feature, please add a test for it. When fixing a bug, please
add a test that demonstrates the fix.

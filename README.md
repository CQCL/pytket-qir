# pytket-qir

`pytket-qir` is a python package, aimed at interafacing QIR programs with `pytket`.

The source code can be found in the corresponding GitHub repository.

## Installation

`pytket-qir` is tested against Python 3.8, 3.9 and 3.10.

The main requirements are:

- `pytket`
- `pyqir`

Standard local installation using `pip`:

```sh
pip install -U .
```

`pytket-qir` has been packaged using `poetry`:

```sh
poetry install
```

_N.B._: `pytket-qir` is tested against x86_64 platforms since `pyqir` is not available for arm64.

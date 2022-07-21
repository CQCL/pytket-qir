# pytket-qir

Public repo for the `pytket-qir` package, aimed at parsing and generating QIR programs to and from pytket circuits.

## Installation

`pytket-qir` is tested against Python 3.8, 3.9 and 3.10.

The main requirements are:

- `pytket`
- `pyqir`

Standard installation using `pip`:

```sh
pip install -U .
```

_N.B._: `pytket-qir` is tested against x86_64 platforms since `pyqir` is not available for arm64.

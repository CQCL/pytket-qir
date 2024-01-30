# Nix support for pytket-qir

## Background

Tket now comes with Nix support. What this means is that the
steps required to launch into an environment with tket and pytket
available on Linux x86-64 and Mac Silicon machines is a single
invocation:

```
nix develop github:CQCL/tket
```

Currently this will build all of the necessary dependencies,
establish the environment, and enter into a shell where
tket and pytket are available for use. Soon we aim to add Cachix,
so that the dependencies are served pre-built to the user.

## Using pytket-qir

The nix.flake in this repository is able to access tket and pytket
from the CQCL/tket nix flake, pinned at the commit and hash noted
in flake.lock (see the Maintenance section). It then exposes
pytket-qir as a package, and provides a development shell containing
pytket-qir.

To launch into an environment with pytket-qir available, use
```
nix develop github:CQCL/pytket-qir
```

from which pytket-qir is now available
```
y$ nix develop github:CQCL/pytket-qir/feature/nix-support

$ python3
Python 3.11.7 (main, Dec  4 2023, 18:10:11) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pytket.circuit import Circuit
>>> from pytket.qir.conversion.api import QIRFormat, pytket_to_qir
>>> c = Circuit(2)
>>> c.H(0)
[H q[0]; ]
>>> c.H(1)
[H q[0]; H q[1]; ]
>>> c.CX(0, 1)
[H q[0]; H q[1]; CX q[0], q[1]; ]
>>> c.H(0)
[H q[0]; H q[1]; CX q[0], q[1]; H q[0]; ]
>>> c.H(1)
[H q[0]; H q[1]; CX q[0], q[1]; H q[0]; H q[1]; ]
>>> print(pytket_to_qir(c, name="example", qir_format=QIRFormat.STRING))
; ModuleID = 'example'
source_filename = "example"

%Qubit = type opaque
%Result = type opaque
; ... and so on
```

This will take some time if tket has not been built on the target machine yet,
as the necessary downloading and building will take place before the environment
is ready. Once we get Cachix it will be much faster, as the builds will be available
from our cache.

## Quirks

At the time of writing, mypy checks for `warn_unused_ignores` are disabled for
nix-only builds, as they lead to false-positives that fail the flake checks.

These are only disabled for the nix version of this repository. This is done
in nix-support/pytket-qir.nix, and is accomplished by modifying the mypy.ini file
at the time of copying it to the Nix store.

## Maintenance

When changes are made, run `nix flake check` to ensure that the nix build works.
If errors are present, run `nix flake check -L` to see the full logs.

The three nix dependencies for this repository are nixpkgs, flake-utils, and tket.

To update all three, simply run:
```
nix flake update
```
and commit the updated flake.lock after verifying with `nix flake check`.

Dependencies can also be updated selectively with e.g.

```
nix flake lock --update-input tket
```

pyqir is not present on the nix store, so we build it manually in nix-support/pyqir.nix.

If the version needs to be updated, follow this procedure:
1. Unset the resulting hashes with `pyqir-hash = "";` and `pytket-cargo-hash = "";`
2. Update pyqir-version to an available tag on the qir-alliance/pyqir github
3. Run `nix flake check`
4. The build will fail with a hash mismatch. Use the hash it provides to replace the blank `pyqir-hash`.
5. Run `nix flake check`
6. The build will fail with a hash mismatch. Use the hash it provides to replace the blank `pyqir-cargo-hash`.
7. Run `nix flake check` again. This time it should succeed.

If the build fails for another reason, further investigation is required.
It is likely down to required change in build steps for pyqir, or could be
a breaking change in pyqir that needs addressing in pytket-qir.

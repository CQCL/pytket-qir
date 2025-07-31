.. currentmodule:: pytket.extensions.qir

Changelog
~~~~~~~~~

0.24.1 (May 2025)
-----------------

* Store more information in :py:exc:`~.ClassicalRegisterWidthError`.

0.24.0 (May 2025)
-----------------

* Define error class for classical registers being too wide.

0.23.0 (May 2025)
-----------------

* Support Python 3.13.
* Update pytket minimium version requirement to 2.4.1.

0.22.0 (April 2025)
-------------------

* Update pytket minimium version requirement to 2.2.0.
* Update pyqir minimium version requirement to 0.10.9.

0.21.1 (March 2025)
-------------------

* Update pytket minimium version requirement to 2.0.1.
* Updated pyqir minimium version requirement to 0.10.7.

0.21.0 (February 2025)
----------------------

* Fix handling of register predicate ops in classical expressions.
* Update pytket minimium version requirement to 2.0.0.

0.20.0 (February 2025)
----------------------

* Updated pytket version requirement to 1.40.

0.19.0 (December 2024)
----------------------

* Updated pytket version requirement to 1.35.
* Updated pyqir version requirement to 0.10.6.
* Add option to generate QIR for azure target

0.17.0 (October 2024)
---------------------

* Update qir generation for wasm functions to work without wasm file handler

0.16.0 (October 2024)
---------------------

* Updated pytket version requirement to 1.34.
* Add support for pytket circuits containing :py:class:`~pytket.circuit.ClExprOp`.
* Always check wasm files

0.15.0 (October 2024)
---------------------

* Add option to generate base profile compatible QIR

0.14.0 (October 2024)
---------------------

* Updated pytket version requirement to 1.33.

0.13.0 (October 2024)
---------------------

* Updated pyqir version requirement to 0.10.4.
* Add option to generate profile compatible QIR
* Updated pytket version requirement to 1.32.
* Add support for BitNot operation

0.12.0 (July 2024)
------------------

* Updated pytket version requirement to 1.30.
* updated pyqir version requirement to 0.10.3.
* Update version requirements on dependencies, removing all upper bounds.
* Speed up conversion
* Sdd additional :py:func:`~.check_circuit` function for checking the
  circuit before converting

0.11.0 (May 2024)
-----------------

* Updated pytket version requirement to 1.28.
* Add support for BitWiseOp.ONE, BitWiseOp.ZERO in conversion

0.10.1 (April 2024)
-------------------

* Updated pytket version requirement to 1.27.

0.9.0 (March 2024)
------------------

* Updated pytket version requirement to 1.26.

0.8.0 (January 2024)
---------------------

* Updated pytket version requirement to 1.24.
* Python 3.12 support added, 3.9 dropped.

0.7.0 (January 2024)
--------------------

* Updated pytket version requirement to 1.23.
* Updated pyqir version requirement to 0.10.0.

0.6.0 (November 2023)
---------------------

* Updated pytket version requirement to 1.22.
* Update measurement to write to register directly
* Remove unused ssa variables generated in output

0.5.0 (November 2023)
---------------------

* Updated pyqir version requirement to 0.9.0.
* Removed dependency of pyqir-generator, pyqir-evaluator and pyqir-parser

0.4.0 (October 2023)
--------------------

* Updated pytket version requirement to 1.21.

0.3.0 (September 2023)
----------------------
* Update pytket version to 1.20

0.2.0 (August 2023)
-------------------
* Fix issue with integer in regular expression
* Add support for wasm in the conversion
* New parameter to set the size of the int parameters of the registers in the qir generation
* Update pytket requirement to 1.19.0rc0
* Update the classical register handling to use i1* pointer
* Add simplification for RangePredicate in case of equal bounds
* Allow conditional circboxes in the circuit
* Add pytket to qir conversion
* Set pyqir version to 0.8.2

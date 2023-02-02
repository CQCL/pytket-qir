Changelog
=========

0.1.5 (February 2023)
---------------------

* Major new features
  * A new `QirConverter` class to convert back and forth QIR and pytket circuits.
    * In QIR to circuit mode:
      * Create and optionally transform a CFG from the QIR program.
      * Use a new `Block` custom type.
      * Optimise by detecting linear chains of blocks and collapse them into
        a single one.
      * Call to the `QirParser` to 
      * Compute a guarding logical expression to generate a circuit composed of conditioned
        subcircuits from each of the QIR blocks.
    * In circuit to QIR mode:
      * Parse the logical expression and compute the corresponding LLVM one.
      * Call to the `QirGenerator` to populate a `pyqir` module for QIR generation.

0.1.4 (November 2022)
---------------------

Minor new features:

* Support for tagged and untagged runtime functions in the parser.
 * `integer_record_output`
 * `bool_record_output`
 * `result_record_output`

* Support for `select` and `zext` functions in the parser.

* Classical arithmetic in the generator.
 * Keep track of created ssa variables for reuse.
 * `reg2const` arithmetic.

* Rebase circuits to target gateset.

Updates:

* `pytket@1.8.0` contains a bugfix for setting bit regisers.


0.1.3 (October 2022)
--------------------

Minor new features:

* WASM support.

Updates:

* Add `py.typed` file.
* Refine release process.
* Add `LICENSE` file.


0.1.2 (July 2022)
-----------------

Updates:

* Add package description and `README.md` to PyPi.
  

0.1.1 (July 2022)
-----------------

Fixes:

* Fix dependency version clash when integrating in `pytket-extensions`.
  
0.1.0 (July 2022)
-----------------

Updates:

* `pytket-qir` is a live public repo and is published on PyPi.


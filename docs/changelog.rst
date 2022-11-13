Changelog
=========

x.y.z (unreleased)
------------------

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


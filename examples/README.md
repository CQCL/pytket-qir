# pytket-qir example notebooks

Here resides the example notebooks of the `pytket-qir` extension.
The `*.ipynb` notebooks are generated from the scripts in `examples/python`
using the `gen-nb` script. The script uses [p2j](https://github.com/remykarem/python2jupyter) tool to generate the notebooks with a Quantinuum logo added to the top.
Notice that the `sed` tool behaves differently on macOS, one can use `gsed` instead of `sed`.  

## How to modify the notebooks

Any change should be done to the corresponding `.py` file in `examples/python`.
For example, in order to modify the `examples/qir_introduction.ipynb` notebook, you need
to change the `examples/python/qir_introduction.py`. After that, you can update the
actual notebook by running the `gen-nb` script.


## Adding new notebooks

To add a new notebook:
1. Create a python file in the `examples/python` folder with the source code for the new notebook.
2. Run the `gen-nb` script to generate the notebook.
3. Commit both the python file and the generated notebook.

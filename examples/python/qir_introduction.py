# pip install pytket~=1.13

# # WASM function calls with pytket
# The WASM module in python allows you to add external classical functions from a compiled web assembly (WASM) to the circuit.

# In the first step you need to read in the wasm file. You can do this when creating the wasm file handler by giving the path to the file. The wasmfilehandler now knows all available functions and the corresponding signatures. If you are not sure about the signatures of the functions of your file you can get a list of them from the wasmfilehandler like shown below. The parameters and result types of the supported functions must be i32. All functions that contain other types will be listed when printing the wasmfilehandler as well, but you can't add them to a circuit.

from pytket import wasm, Circuit, Bit

wfh = wasm.WasmFileHandler("testfile.wasm")
print("wasm file uid:")
print(wfh)

print("\n\nwasm file repr:")
print(repr(wfh))

# In the next step we want to add some of the classical function calls to a circuit. We will start with adding the function "add_one" to read in for the first parameter from Bit(0) and write the result to Bit(1). The length of the two list giving the number of bits needs to be the number of parameters and the number of results.

c = Circuit(0, 8)

c.add_wasm(
    "add_one",  # name of the function
    wfh,  # wasm file handler
    [1],  # number of bits in each of the parameter i32
    [1],  # number of bits in each of the result i32
    [Bit(0), Bit(1)],
)  # list of bits where the wasm op will be added to

# If you want to have more than one bit per parameter, you can add that in the following way. This will add the function "add_one" to read in for the first parameter from Bit(0) and Bit(1) and write the result to Bit(2), Bit(3) and Bit(4).

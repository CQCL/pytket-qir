# pip install pytket~=1.13

# # QIR generation from a pytket circuit

# For this you should install pytket, pytket-quantinuum and pytket-qir in the newest avialble version

from pytket.qir import pytket_to_qir, ReturnTypeQIR

from pytket import Circuit

circ = Circuit(3)

circ.H(0)

qir_string = pytket_to_qir(circ, returntype=ReturnTypeQIR.STRING)

print(qir_string)

from pytket import wasm, Bit

wfh = wasm.WasmFileHandler("testfile.wasm")

# In the next step we want to add some of the classical function calls to a circuit. We will start with adding the function "add_one" to read in for the first parameter from Bit(0) and write the result to Bit(1). The length of the two list giving the number of bits needs to be the number of parameters and the number of results.

c = Circuit(0, 8)
a = c.add_c_register("a", 64)
b = c.add_c_register("b", 64)

c.add_wasm_to_reg(
    "add_one",
    wfh,
    [a],
    [b],
)  # list of bits where the wasm op will be added to

# If you want to have more than one bit per parameter, you can add that in the following way. This will add the function "add_one" to read in for the first parameter from Bit(0) and Bit(1) and write the result to Bit(2), Bit(3) and Bit(4).

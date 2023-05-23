# pip install pytket~=1.13

# # QIR generation from a pytket circuit

# For this you should install pytket, pytket-quantinuum and pytket-qir in the newest avialble version

from pytket.qir import pytket_to_qir, ReturnTypeQIR

from pytket import Circuit

circ = Circuit(3)

circ.H(0)

qir_string = pytket_to_qir(circ, returntype=ReturnTypeQIR.STRING)

print(qir_string)

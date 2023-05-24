# pip install pytket~=1.13

# # QIR generation from a pytket circuit

# For this you should install pytket-quantinuum and pytket-qir in the newest available versions.

from pytket.qir import pytket_to_qir, QIRFormat

from pytket import Circuit

circ = Circuit(3)

circ.H(0)

qir_string = pytket_to_qir(circ, returntype=QIRFormat.STRING)

print(qir_string)

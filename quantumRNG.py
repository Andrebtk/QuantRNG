import sys
from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator
from qiskit import Aer

from libRNG import maxCount, bin2Dec, XY


maxInput = int(input("Generate a number between 0 and: "))
n=0


for i in range(maxInput):
    if 2**i < maxInput:
        n+=1



qc = QuantumCircuit(n)

for i in range(n):
    qc.h(i)

qc.measure_all()

if len(sys.argv) > 1:
    for i in sys.argv:
        if i == '-circuit':
            print(qc)

backend = Aer.get_backend('aer_simulator')
res = backend.run(qc).result().get_counts()



print("Random number generated: "+str(bin2Dec(maxCount(res, n))))


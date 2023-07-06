<<<<<<< HEAD
import sys
from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator
from qiskit import Aer


=======
>>>>>>> eeaa6d60ddc6d866cc02d3b202b963e36482d951
def maxCount(res, nQubit):
    maxF = (nQubit)*"0"
    for i in res:
        if int(res[i]) > int(res[maxF]):
            maxF = i            
    return maxF

<<<<<<< HEAD

def bin2Dec(bin):
    return int(bin,2)


def QuantRNG(maxInput):
    n=0
    for i in range(maxInput):
        if 2**i < maxInput:
            n+=1

    maxQubitValue = 2**n
    delta = maxQubitValue - maxInput

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

    result = bin2Dec(maxCount(res, n))

    if result > delta:
        result-=delta

    return result


=======
def bin2Dec(bin):
    return int(bin,2)

>>>>>>> eeaa6d60ddc6d866cc02d3b202b963e36482d951
#Not used yet
def XY(res):
    xData = []
    yData = []

    for i in res:
        yData.append(int(res[i]))
        xData.append(int(i))
<<<<<<< HEAD
    return (xData, yData)
=======
    return (xData, yData)
>>>>>>> eeaa6d60ddc6d866cc02d3b202b963e36482d951

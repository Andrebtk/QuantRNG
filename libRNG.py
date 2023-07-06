import sys
from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator
from qiskit import Aer


def maxCount(res, nQubit):
    maxF = (nQubit)*"0"
    for i in res:
        if int(res[i]) > int(res[maxF]):
            maxF = i            
    return maxF


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

def QuantRNGint(minIn, maxIn):

    
    if minIn != 0:
        maxInput = maxIn - minIn
    else:
        maxInput=maxIn

    result = QuantRNG(maxInput)

    if minIn != 0:
            result += minIn
    
    return result

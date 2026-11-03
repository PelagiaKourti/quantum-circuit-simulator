import numpy as np
from simulator import QuantumCircuit

def test_bell():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cnot(0, 1)
    assert np.allclose(qc.probabilities(), [0.5, 0, 0, 0.5])
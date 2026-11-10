import numpy as np
from simulator import QuantumCircuit


def test_bell():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cnot(0, 1)
    assert np.allclose(qc.probabilities(), [0.5, 0, 0, 0.5])

def test_ghz():
    qc = QuantumCircuit(3)
    qc.h(0)             # |000>                -> (|000>+|100>) /sqrt2
    qc.cnot(0,1)        # (|000>+|100>) /sqrt2 -> (|000>+|110>) /sqrt2
    qc.cnot(1,2)        # (|000>+|110>) /sqrt2 -> (|000>+|111>) /sqrt2
    expected = np.zeros(8)
    expected[0] = 0.5; expected[7] = 0.5; 
    assert np.allclose(qc.probabilities(), expected)

def test_cnot_non_adjacent():
    qc = QuantumCircuit(3)
    qc.x(0)
    qc.cnot(0,2)
    expected = np.zeros(8)
    expected[5] = 1
    assert np.allclose(qc.probabilities(), expected)

def test_hh_is_identity():
    qc = QuantumCircuit(1)
    qc.h(0); qc.h(0)
    assert np.allclose(qc.state, [1,0])   # since |0> = [1,0]

def test_tt_equals_s():    # test that two T gates give a S gate
    a = QuantumCircuit(1); a.h(0); a.t(0); a.t(0)
    b = QuantumCircuit(1); b.h(0); b.s(0)
    assert np.allclose(a.state, b.state)  # unlike ==, that fails if it is not exactly the same

def test_ss_equals_z():    #test that two S gates give a Z gate
    c = QuantumCircuit(1); c.h(0); c.s(0); c.s(0)
    d = QuantumCircuit(1); d.h(0); d.z(0)
    assert np.allclose(c.state,d.state) 

def test_measure_bell():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cnot(0, 1)
    counts = qc.measure(1000)
    assert set(counts.keys()) == {'00', '11'}

def test_rx_pi():
    qc = QuantumCircuit(1); qc.rp("x", 0, np.pi)
    assert np.allclose(qc.probabilities(), [0,1])

def test_ry_half_pi():
    qc = QuantumCircuit(1); qc.rp("y", 0, np.pi/2)
    assert np.allclose(qc.state, [1/ np.sqrt(2), 1 / np.sqrt(2)])

def test_ry_probability():
    for theta in [0, 0.3, 1, np.pi/2, 2, np.pi]:
        qc = QuantumCircuit(1); qc.rp("y", 0 , theta)
        assert np.isclose(qc.probabilities()[1], np.sin(theta /2)**2 )

def test_rz_keeps_probabilities():
    for theta in [0, 0.3, 1, np.pi/2, 2, np.pi]:
        qc = QuantumCircuit(1); qc.rp("z", 0, theta)
        assert np.allclose(qc.probabilities(), [1,0])
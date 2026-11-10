# Quantum Circuit Simulator

A statevector quantum circuit simulator written from scratch in Python (NumPy).

I am building it while studying *Quantum Computation and Quantum Information* (by Nielsen & Chuang).


## Features

- Circuits of any number of qubits `n`, starting in |00...0>
- Single-qubit gates **H**, **X**, **Y**, **Z**, **S**, **T** on any qubit
- Rotation gates **Rx(θ)**, **Ry(θ)**, **Rz(θ)** on any qubit, through one method: `rp(axis, qubit, theta)`
- **CNOT** between any two qubits, including non-adjacent ones and with control after target
- Exact outcome **probabilities**
- Simulated **measurement** with a chosen number of shots
- Automated tests with `pytest`


## Example

```python
qc = QuantumCircuit(2)
qc.h(0)
qc.cnot(0, 1)
print(qc.measure(1000))    # e.g. {'00': 503, '11': 497}

qc = QuantumCircuit(1)
qc.rp("y", 0, np.pi / 2)   # rotation by π/2 around the y-axis
print(qc.state)            # [0.707, 0.707], the |+> state
```


## Tests

```bash
pip install pytest
pytest
```


## Roadmap

- [x] Gates S, T, Y
- [x] Rotation gates Rx, Ry, Rz
- [x] Tests for gate identities (HH = I, TT = S, SS = Z) and rotations
- [ ] Toffoli gate
- [ ] Protocols: quantum teleportation, superdense coding
- [ ] Algorithms: Deutsch–Jozsa, Bernstein–Vazirani, Grover search, Quantum Fourier Transform
- [ ] Faster gate application without building full matrices
- [ ] Circuit optimisation with the ZX-calculus (PyZX), using this simulator to check that optimised circuits are equivalent to the originals


## About

I am a mathematician (BSc and MSc, Aristotle University of Thessaloniki, Greece).
My MSc thesis, *Geometry of Quantum Computing*, covered quantum information geometry and circuit optimisation with the ZX-calculus.
# Quantum Circuit Simulator

A statevector quantum circuit simulator written from scratch in Python (NumPy).

I am building it while studying *Quantum Computation and Quantum Information* (by Nielsen & Chuang). 


## Features

- Circuits of any number of qubits `n`, starting in |00...0>
- Single-qubit gates **H**, **X**, **Z** on any qubit
- **CNOT** between any two qubits, including non-adjacent ones and with control after target
- Exact outcome **probabilities**
- Simulated **measurement** with a chosen number of shots



## Roadmap

- Automated tests with `pytest`
- More gates: S, T, Y, rotations, Toffoli
- Protocols: quantum teleportation, superdense coding
- Algorithms: Deutsch–Jozsa, Grover search, Quantum Fourier Transform
- Faster gate application without building full matrices
- Circuit optimisation with the ZX-calculus (PyZX), using this simulator to check that optimised circuits are equivalent to the originals


## About

I am a mathematician (BSc and MSc, Aristotle University of Thessaloniki, Greece). 
My MSc thesis, *Geometry of Quantum Computing*, covered quantum information geometry and circuit optimisation with the ZX-calculus.
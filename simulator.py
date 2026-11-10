import numpy as np 
import collections as col

X = np.array([[0,1], [1,0]])
Y = np.array([[0,-1j], [1j, 0]])
Z = np.array([[1,0],[0,-1]])
I2 = np.eye(2)

class QuantumCircuit():
    def __init__(self,n):
        self.n = n
        self.state = np.zeros(2 ** n, dtype=complex)   
        self.state[0] = 1                            
    
    #Identity gate
    def _apply_single(self, gate, k):   
        I = np.eye(2)
        mats = [gate if q == k else I for q in range(self.n)]
        self.state = self._kron_list(mats) @ self.state
    
    #Hadamard gate
    def h(self, k):
        H = np.array([[1,1],[1,-1]]) / np.sqrt(2)
        self._apply_single(H,k)
    
    #X gate
    def x(self,k):
        self._apply_single(X,k)
    
    #Y gate   
    def y(self,k):
        self._apply_single(Y,k)
    
    #Z gate
    def z(self,k):
        self._apply_single(Z,k)
    
    #S gate, S**2 = Z
    def s(self,k):
        S = np.diag([1, 1j])
        self._apply_single(S,k)
    
    #T gate, T**2 = S
    def t(self,k):
        T = np.diag([1, np.exp(1j * np.pi /4)])
        self._apply_single(T,k)    
    
    #R_X, R_Y, R_Z:
    def rp(self, P, k, theta):
        pauli = {"x" : X, "y" : Y, "z" : Z}
        RP = np.cos(theta/2) * I2 - 1j * np.sin(theta/2) * pauli[P]
        self._apply_single(RP, k)
    
    #tensor product of matrices
    def _kron_list(self, mats):
        M = np.array([[1]])
        for A in mats:
            M = np.kron(M, A)
        return M
    
    #CNOT gate
    def cnot(self, control, target):
        P0 = np.array([[1,0],[0,0]])
        P1 = np.array([[0,0],[0,1]])
        
        #Example for 3 qubits with control=0, target=2:
        #term0 = [P0, I, I]
        #term1 = [P1, I, X]
        #M = self._kron_list(term0) + self._kron_list(term1)
        
        
        #for n qubits with control=k1, target=k2:
        term0 = [P0 if q == control else I2 for q in range(self.n)]
        term1 = []
        for q in range(self.n):
            if q == control:
                term1.append(P1)
            elif q == target:
                term1.append(X)
            else:
                term1.append(I2)
        M = self._kron_list(term0) + self._kron_list(term1)
        self.state = M @ self.state


    #probabilities
    def probabilities(self):
        return np.abs(self.state) ** 2   

    #measurement
    def measure(self, shots):
        p = self.probabilities()
        results = np.random.choice(2 ** self.n, size=shots, p=p)
        bits = [format(r, f'0{self.n}b') for r in results]        
        return dict(col.Counter(bits))


if __name__ == "__main__":
    #examples
    # Bell: [0.5, 0, 0, 0.5]
    qc = QuantumCircuit(2)
    qc.h(0); qc.cnot(0, 1)
    print(qc.probabilities())  
    print(qc.measure(1000))   

    # GHZ: [0.5, 0, 0, 0, 0, 0, 0, 0.5]
    qc = QuantumCircuit(3)
    qc.h(0); qc.cnot(0, 1); qc.cnot(1, 2)
    print(qc.probabilities())   

    #|101> with probability 1
    qc = QuantumCircuit(3)
    qc.x(0); qc.cnot(0, 2)
    print(qc.probabilities())   
    
    qc = QuantumCircuit(1)
    qc.rp("y", 0, np.pi / 2)  #that is, |+>
    print(qc.state) 
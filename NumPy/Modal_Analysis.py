import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

# Beam properties
E = 210e9          # Young's modulus (Pa)
rho = 7800         # density (kg/m3)
L = 1.0            # beam length (m)
b = 0.02           # width
h = 0.002          # thickness

A = b*h
I = b*h**3/12

# Discretization
N = 50
dx = L/(N-1)

# Mass matrix
M = rho*A*np.eye(N)

# Stiffness matrix
K = np.zeros((N,N))

for i in range(2,N-2):
    K[i,i-2] = 1
    K[i,i-1] = -4
    K[i,i]   = 6
    K[i,i+1] = -4
    K[i,i+2] = 1

K = (E*I/dx**4)*K

# Apply cantilever BC
K = K[2:,2:]
M = M[2:,2:]

# Solve eigenvalue problem
eigvals, eigvecs = la.eig(K,M)

omega = np.sqrt(np.real(eigvals))
freq = omega/(2*np.pi)

# Sort frequencies
freq = np.sort(freq)

print("Natural Frequencies (Hz):")
print(freq[:5])

# Plot first mode shape
mode = eigvecs[:,0]

x = np.linspace(0,L,len(mode))

plt.plot(x,mode)
plt.title("First Mode Shape")
plt.xlabel("Beam Length")
plt.ylabel("Displacement")
plt.show()


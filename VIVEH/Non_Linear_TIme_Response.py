import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.fft import fft, fftfreq

# -----------------------------
# Parameters (Table 1)
# -----------------------------
mp = 0.07      # pendulum mass (kg)
mB = 0.16      # tip mass (kg)
kB1 = 50       # linear bending stiffness (N/m)
kB3 = -2.5e3   # cubic stiffness (N/m^3)
cB = 0.0045    # bending damping (Ns/m)
kP = 0.43      # torsional stiffness (Nm/rad)
cP = 0.0015    # torsional damping (Nms/rad)
L = 0.207      # pendulum length (m)
g = 9.8        # gravity

Ae = 0.004     # base excitation amplitude (m)
omega = 2*np.pi*1.8  # near torsional resonance

# -----------------------------
# ODE System
# state = [y, y_dot, phi, phi_dot]
# -----------------------------
def vib_system(t, state):
    y, y_dot, phi, phi_dot = state
    
    y_base = Ae*np.sin(omega*t)
    y_base_dot = Ae*omega*np.cos(omega*t)
    y_base_ddot = -Ae*(omega**2)*np.sin(omega*t)
    
    # Effective RHS terms
    M11 = mp + mB
    M12 = mp*L*np.cos(phi)
    M21 = mp*np.cos(phi)
    M22 = mp*L
    
    # Nonlinear forces
    F1 = -mp*L*(phi_dot**2)*np.sin(phi) - kB1*y - kB3*y**3 - cB*y_dot
    F2 = -mp*g*np.sin(phi) - (kP/L)*phi - (cP/L)*phi_dot
    
    # Solve 2x2 system for accelerations
    M = np.array([[M11, M12],
                  [M21, M22]])
    
    F = np.array([F1,
                  F2])
    
    acc = np.linalg.solve(M, F)
    
    y_ddot = acc[0]
    phi_ddot = acc[1]
    
    return [y_dot, y_ddot, phi_dot, phi_ddot]

# -----------------------------
# Time Integration
# -----------------------------
t_span = (0, 40)
t_eval = np.linspace(*t_span, 8000)

initial_state = [0.0, 0.0, 0.01, 0.0]

sol = solve_ivp(vib_system, t_span, initial_state, t_eval=t_eval)

y = sol.y[0]
phi = sol.y[2]
t = sol.t

## Time Domain Repsonse

plt.figure(figsize=(10,6))
plt.plot(t, y, label='Bending (y)')
plt.plot(t, phi, label='Torsion (phi)')
plt.xlabel("Time (s)")
plt.ylabel("Response")
plt.legend()
plt.grid()
plt.title("Time Response")
plt.show()

## Phase Portraits

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(y, sol.y[1])
plt.xlabel("y")
plt.ylabel("y_dot")
plt.title("Bending Phase Portrait")
plt.grid()

plt.subplot(1,2,2)
plt.plot(phi, sol.y[3])
plt.xlabel("phi")
plt.ylabel("phi_dot")
plt.title("Torsion Phase Portrait")
plt.grid()

plt.tight_layout()
plt.show()

## Frequency Spectrum

dt = t[1] - t[0]
Y_fft = fft(y)
freq = fftfreq(len(t), dt)

plt.figure(figsize=(8,5))
plt.plot(freq[:len(freq)//2], np.abs(Y_fft[:len(freq)//2]))
plt.xlim(0,5)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("Frequency Spectrum of Bending")
plt.grid()
plt.show()

## Frequency Sweep

freq_range = np.linspace(0.5, 4.5, 40)
max_amp = []

for f in freq_range:
    omega = 2*np.pi*f
    
    sol = solve_ivp(vib_system, (0,40), initial_state, 
                    t_eval=np.linspace(0,40,6000))
    
    steady = sol.y[0][-2000:]
    max_amp.append(np.max(np.abs(steady)))

plt.plot(freq_range, max_amp)
plt.xlabel("Excitation Frequency (Hz)")
plt.ylabel("Max Bending Amplitude")
plt.title("Frequency Response (Softening)")
plt.grid()
plt.show()

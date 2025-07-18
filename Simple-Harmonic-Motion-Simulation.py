# Simple-Harmonic-Motion-Simulation
import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = eval(input("Amplitude:"))                  # Amplitude
k = eval(input("Spring Constant:"))            # Spring constant
m = eval(input("Mass:"))                       # Mass
omega = np.sqrt(k/m)
phi = 0          # Phase

# Time array
t = np.linspace(0, 10, 500)
x = A * np.cos(omega * t + phi)

# Plot
plt.figure(figsize=(8, 4))
plt.plot(t, x)
plt.title('Simple Harmonic Motion: Mass-Spring System')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid(True)
plt.show()
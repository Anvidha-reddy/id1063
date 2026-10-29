import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os

# Symbolic Laplace transform verification
s, t, tau = sp.symbols('s t tau', positive=True, real=True)

U1 = sp.exp(-2*s)/s
U2 = 1/s**2
X = sp.simplify(U1 * U2)

print("L{u(t-2)} =", U1)
print("L{t*u(t)} =", U2)
print("X(s) =", X)
print("Option D:", X == sp.exp(-2*s)/s**3)

# Numerical convolution
dt = 0.001
time = np.arange(0, 10, dt)

f = np.heaviside(time - 2, 0)
g = time

conv = np.convolve(f, g, mode='full') * dt
time_conv = np.arange(len(conv)) * dt

# Plot signals and convolution
fig, ax = plt.subplots(3, 1, figsize=(9, 10))

ax[0].plot(time, f)
ax[0].set_title(r'$u(t-2)$')
ax[0].set_ylabel('Amplitude')
ax[0].grid(True)

ax[1].plot(time, g)
ax[1].set_title(r'$t u(t)$')
ax[1].set_ylabel('Amplitude')
ax[1].grid(True)

ax[2].plot(time_conv, conv)
ax[2].set_title(r'$u(t-2)*(t u(t))$')
ax[2].set_xlabel('Time (t)')
ax[2].set_ylabel('Amplitude')
ax[2].set_xlim(0, 10)
ax[2].grid(True)

plt.tight_layout()

filename = os.path.abspath("laplace_convolution.png")
plt.savefig(filename, dpi=200)
plt.close()

# Open the plot automatically; no plt.show()
subprocess.run(["termux-open", filename])

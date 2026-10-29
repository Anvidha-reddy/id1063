import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os

# Surface: z^2 = 2x^2 - y^2
x = np.linspace(-2, 2, 150)
y = np.linspace(-2, 2, 150)
X, Y = np.meshgrid(x, y)

Z2 = 2*X**2 - Y**2
Z = np.where(Z2 >= 0, np.sqrt(np.maximum(Z2, 0)), np.nan)

# Given point
P = np.array([1, 0, np.sqrt(2)])

# Gradient of F = 2x^2 - y^2 - z^2
grad = np.array([4*P[0], -2*P[1], -2*P[2]])

# Unit normal
n = grad / np.linalg.norm(grad)

print("Point P =", P)
print("Gradient =", grad)
print("Unit normal =", n)
print("Opposite unit normal =", -n)

# Plot
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

# Both halves of the surface
ax.plot_surface(X, Y, Z, alpha=0.45, cmap='viridis')
ax.plot_surface(X, Y, -Z, alpha=0.45, cmap='viridis')

# Point P
ax.scatter(*P, color='red', s=80, label='Point P')

# Normal vector, scaled for visibility
scale = 0.8
ax.quiver(*P, *(scale*n), color='black',
          linewidth=3, arrow_length_ratio=0.2,
          label='Unit normal direction')

# Opposite normal
ax.quiver(*P, *(-scale*n), color='orange',
          linewidth=3, arrow_length_ratio=0.2,
          label='Opposite normal direction')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(r'Surface $z^2=2x^2-y^2$ with normal at $P$')
ax.legend()

plt.tight_layout()

# Save and open automatically
filename = os.path.abspath("normal_plot.png")
plt.savefig(filename, dpi=200)
plt.close()

subprocess.Popen(["xdg-open", filename])

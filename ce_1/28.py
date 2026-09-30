import os
import sys
import subprocess
import numpy as np
import matplotlib.pyplot as plt

# 1. Quadratic Form Matrix and Linear Terms Setup
# 5x^2 + 4xy + y^2 - 46x - 20y + 109 = 0
A = np.array([[5, 2], 
              [2, 1]], dtype=float)

B = np.array([-46, -20], dtype=float)
c = 109.0

# 2. Factorize Matrix A into M^T @ M to find line coefficients
# A = M^T M where M = [[1, 1], [3, 1]]
M = np.array([[1, 1], 
              [3, 1]], dtype=float)

# Solve for constant vector d in: -2 * M^T @ d = B  =>  M^T @ d = -B / 2
d = np.linalg.solve(M.T, -B / 2.0)

print("Matrix representation of the system:")
print(f"M =\n{M}")
print(f"d = {d}")
print(f"Line 1 equation: {M[0,0]}x + {M[0,1]}y = {d[0]}")
print(f"Line 2 equation: {M[1,0]}x + {M[1,1]}y = {d[1]}\n")

# 3. Solve for (x, y) using Matrix Inversion: x_vec = M^(-1) * d
M_inv = np.linalg.inv(M)
xy = M_inv @ d

x_sol, y_sol = xy[0], xy[1]
ans = int(round(x_sol**3 + y_sol**3))

print(f"Intersection point (x, y): ({x_sol:.1f}, {y_sol:.1f})")
print(f"Value of x^3 + y^3: {ans}\n")

# 4. Generate Plot
x_vals = np.linspace(0, 6, 200)

# Line 1: x + y = 7  =>  y = 7 - x
y1_vals = d[0] - M[0,0] * x_vals

# Line 2: 3x + y = 13 => y = 13 - 3x
y2_vals = (d[1] - M[1,0] * x_vals) / M[1,1]

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y1_vals, label=r'Line 1: $x + y - 7 = 0$', color='blue', linewidth=2)
plt.plot(x_vals, y2_vals, label=r'Line 2: $3x + y - 13 = 0$', color='green', linewidth=2)

# Mark the intersection point (3, 4)
plt.scatter([x_sol], [y_sol], color='red', s=100, zorder=5, label=f'Intersection (x={int(x_sol)}, y={int(y_sol)})')
plt.text(x_sol + 0.1, y_sol + 0.2, f'({int(x_sol)}, {int(y_sol)})\n$x^3+y^3={ans}$', fontsize=11, fontweight='bold', color='darkred')

# Formatting
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlim([0, 6])
plt.ylim([0, 10])
plt.xlabel('$x$', fontsize=12)
plt.ylabel('$y$', fontsize=12)
plt.title('Q.28: Intersecting Lines from Quadratic System', fontsize=14, pad=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right', fontsize=10)

# Save image as 28.png
image_filename = '28.png'
plt.savefig(image_filename, dpi=300, bbox_inches='tight')
plt.close()

# 5. Automatically open the image via subprocess
if sys.platform.startswith('win'):
    os.startfile(image_filename)
elif sys.platform.startswith('darwin'):
    subprocess.run(['open', image_filename])
else:
    subprocess.run(['xdg-open', image_filename])


import os
import sys
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Create grid of x1 and x3 values
x1_vals = np.linspace(-5, 5, 50)
x3_vals = np.linspace(-5, 5, 50)
X1, X3 = np.meshgrid(x1_vals, x3_vals)

# Plane 1: x1 + x2 + x3 = 0  =>  x2 = -x1 - x3
X2_plane1 = -X1 - X3

# Plane 2: x1 + 2*x3 = 0  =>  x1 = -2*x3 (independent of x2)
x2_vals = np.linspace(-5, 5, 50)
X2_plane2, X3_plane2 = np.meshgrid(x2_vals, x3_vals)
X1_plane2 = -2 * X3_plane2

# Intersecting Line: [x1, x2, x3] = t * [-2, 1, 1]
t = np.linspace(-2.5, 2.5, 100)
line_x1 = -2 * t
line_x2 = 1 * t
line_x3 = 1 * t

# 2. Plotting
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Surface 1: Cyan
surf1 = ax.plot_surface(X1, X2_plane1, X3, alpha=0.4, color='cyan', edgecolor='none')
surf1._facecolors2d = surf1._edgecolors2d

# Surface 2: Magenta
surf2 = ax.plot_surface(X1_plane2, X2_plane2, X3_plane2, alpha=0.4, color='magenta', edgecolor='none')
surf2._facecolors2d = surf2._edgecolors2d

# Intersecting Line: Thick Red Line
line, = ax.plot(line_x1, line_x2, line_x3, color='red', linewidth=4, label='Intersecting Line (x1 = -2t, x2 = t, x3 = t)')

# Origin Point
ax.scatter([0], [0], [0], color='black', s=80, label='Origin (0, 0, 0)')
image_filename = '12.pngimage_filename = '12.png''
# 3. Add 3D Text Labels directly onto the geometric structures
ax.text(3, -5, 2, 'Plane 1: $x_1 + x_2 + x_3 = 0$', color='blue', fontsize=11, fontweight='bold')
ax.text(-4, 3, 2, 'Plane 2: $x_1 + 2x_3 = 0$', color='purple', fontsize=11, fontweight='bold')
ax.text(2, -2, -2, 'Intersection Line', color='darkred', fontsize=11, fontweight='bold')

# Formatting Labels & Axes
ax.set_xlabel('$x_1$', fontsize=12)
ax.set_ylabel('$x_2$', fontsize=12)
ax.set_zlabel('$x_3$', fontsize=12)
ax.set_title('Geometric Solution: Intersection of Two Planes Forming a Line', fontsize=14, pad=15)
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

# Custom legend entries
ax.plot([], [], color='cyan', alpha=0.6, linewidth=8, label='Plane 1: x1 + x2 + x3 = 0')
ax.plot([], [], color='magenta', alpha=0.6, linewidth=8, label='Plane 2: x1 + 2x3 = 0')
ax.legend(loc='upper right', fontsize=10)

image_filename = '12.png'
plt.savefig(image_filename, dpi=300, bbox_inches='tight')
plt.close()

# 4. Open the generated image immediately using subprocess
if sys.platform.startswith('win'):
    os.startfile(image_filename)  # Windows
elif sys.platform.startswith('darwin'):
    subprocess.run(['open',image_filename])  # macOS
else:
    subprocess.run(['xdg-open',image_filename])  # Linux


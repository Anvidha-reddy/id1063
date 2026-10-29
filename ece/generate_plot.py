import numpy as np
import matplotlib.pyplot as plt
import os
import webbrowser

# 1. Grid setup for 3D surface
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# 2. Surface equation: z^2 = 2x^2 - y^2  =>  z = +/- sqrt(2x^2 - y^2)
Z2 = 2 * X**2 - Y**2
Z2_masked = np.where(Z2 >= 0, Z2, np.nan)
Z_pos = np.sqrt(Z2_masked)
Z_neg = -np.sqrt(Z2_masked)

# 3. Create 3D figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot positive and negative sheets of the surface
ax.plot_surface(X, Y, Z_pos, cmap='coolwarm', alpha=0.6, edgecolor='none')
ax.plot_surface(X, Y, Z_neg, cmap='coolwarm', alpha=0.6, edgecolor='none')

# Point P(1, 0, sqrt(2))
px, py, pz = 1.0, 0.0, np.sqrt(2)
ax.scatter([px], [py], [pz], color='red', s=120, label=f'Point P (1, 0, {np.sqrt(2):.2f})', zorder=5)

# Unit Normal Vector (Option D): n = (sqrt(2)i - k) / sqrt(3)
nx, ny, nz = np.sqrt(2)/np.sqrt(3), 0.0, -1.0/np.sqrt(3)

# Plot normal vector arrow at point P
scale = 1.2
ax.quiver(px, py, pz, 
          nx * scale, ny * scale, nz * scale, 
          color='black', linewidth=3, arrow_length_ratio=0.15, 
          label=f'Normal Vector n = ({nx:.2f})i + ({nz:.2f})k')

# Verification annotation box directly on the plot
text_str = (
    "Option (D) Verified:\n"
    "n = (sqrt(2)i - k) / sqrt(3)\n"
    f"  = ({nx:.3f})i + ({nz:.3f})k"
)
ax.text2D(0.05, 0.82, text_str, transform=ax.transAxes, fontsize=12,
          bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9))

# Styling and view orientation
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Surface z^2 = 2x^2 - y^2 with Unit Normal Vector', fontsize=14)
ax.legend(loc='upper right')
ax.view_init(elev=20, azim=45)

# Save figure to file
image_path = 'surface_normal_plot.png'
plt.savefig(image_path, dpi=300, bbox_inches='tight')

# Automatically open the saved image directly in default viewer
webbrowser.open('file://' + os.path.realpath(image_path))

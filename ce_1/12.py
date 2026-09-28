1 - x3
X2_plane1 = -X1 - X3

# Plane 2: x1 + 2*x3 = 0  =>  x2 can be anything (independent of x1 and x3)
# To plot Plane 2 as a surface, x1 is fixed by x3: x1 = -2*x3
x2_vals = np.linspace(-5, 5, 50)
X2_plane2, X3_plane2 = np.meshgrid(x2_vals, x3_vals)
X1_plane2 = -2 * X3_plane2

# Intersecting Line: [x1, x2, x3] = t * [-2, 1, 1]
t = np.linspace(-2.5, 2.5, 100)
line_x1 = -2 * t
line_x2 = 1 * t
line_x3 = 1 * t

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot Plane 1 (Cyan)
ax.plot_surface(X1, X2_plane1, X3, alpha=0.5, color='cyan', edgecolor='none', label='Plane 1: x1 + x2 + x3 = 0')

# Plot Plane 2 (Magenta)
ax.plot_surface(X1_plane2, X2_plane2, X3_plane2, alpha=0.5, color='magenta', edgecolor='none', label='Plane 2: x1 + 2*x3 = 0')

# Plot the Intersecting Line (Red)
ax.plot(line_x1, line_x2, line_x3, color='red', linewidth=4, label='Intersecting Line')

# Plot Origin Point
ax.scatter([0], [0], [0], color='black', s=50, label='Origin (0,0,0)')

# Formatting plot
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$x_3$')
ax.set_title('Intersection of Two Planes Forming a Line')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

plt.savefig('12.png', dpi=300, bbox_inches='tight')
plt.close()


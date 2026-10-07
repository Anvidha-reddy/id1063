import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os
import platform

# 1. Values calculated from differentiability conditions at x = 1
a = 5.0
b = -2.0

print(f"Value of a: {a}")
print(f"Value of b: {b}")

# 2. Generate x values for plotting
x_left = np.linspace(-1, 1, 200)
x_right = np.linspace(1, 2.5, 200)

y_left = a * x_left + b
y_right = x_right**3 + x_right**2 + 1

# 3. Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_left, y_left, 'r--', label=f'f(x) = {a}x + ({b})  [x < 1]', linewidth=2)
plt.plot(x_right, y_right, 'b-', label=f'f(x) = x³ + x² + 1  [x ≥ 1]', linewidth=2)
plt.plot(1, 3, 'go', markersize=8, label='Boundary Point (1, 3)')

plt.title("Smooth Transition of Differentiable Function $f(x)$ at $x = 1$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axvline(x=1, color='gray', linestyle=':', alpha=0.7)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# 4. Save the figure to a file
filename = "plot.png"
plt.savefig(filename, bbox_inches='tight')
plt.close() 

# 5. Automatically open the saved file using subprocess (Cross-Platform)
current_os = platform.system()

if current_os == "Windows":
    os.startfile(filename)  # Native Windows viewer launcher
elif current_os == "Darwin":  # macOS
    subprocess.run(["open", filename])
else:  # Linux / Unix
    subprocess.run(["xdg-open", filename])


import sys
import subprocess
import numpy as np
import matplotlib.pyplot as plt

# Define the CDF function F(x)
def F(x):
    x = np.asarray(x, dtype=float)
    return np.piecewise(
        x,
        [x < 1, (x >= 1) & (x <= 4), x > 4],
        [0, lambda x: (x**3 - 1) / 63, 1]
    )

# Setup figure parameters
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=150)

# Generate points and curve
x_full = np.linspace(0, 5, 1000)
y_full = F(x_full)
ax.plot(x_full, y_full, label=r'$F(x) = \frac{x^3 - 1}{63},\ 1 \leq x \leq 4$', color='#1f77b4', linewidth=2.5)

# Boundary dashed lines at x = 1 and x = 4
ax.axvline(x=1, color='gray', linestyle='--', linewidth=1.2)
ax.axvline(x=4, color='gray', linestyle='--', linewidth=1.2)

# Reference dotted lines for x = 2 and x = 3
f2_val = float(F(2.0))
f3_val = float(F(3.0))

ax.axvline(x=2, color='#d62728', linestyle=':', linewidth=1.2)
ax.axvline(x=3, color='#d62728', linestyle=':', linewidth=1.2)
ax.axhline(y=f2_val, color='#d62728', linestyle=':', linewidth=1.2)
ax.axhline(y=f3_val, color='#d62728', linestyle=':', linewidth=1.2)

# Highlight point values on the curve
ax.scatter([2, 3], [f2_val, f3_val], color='#d62728', zorder=5)

# Text annotations
ax.annotate(r'$F(2) = \frac{7}{63} \approx 0.111$', (2, f2_val), textcoords="offset points", xytext=(10, 10), fontsize=10)
ax.annotate(r'$F(3) = \frac{26}{63} \approx 0.413$', (3, f3_val), textcoords="offset points", xytext=(10, 10), fontsize=10)

ax.text(0.5, 0.05, r'$F(x) = 0$', fontsize=10, color='gray', ha='center')
ax.text(4.5, 0.95, r'$F(x) = 1$', fontsize=10, color='gray', ha='center')

# Graph aesthetics
ax.set_title('Cumulative Distribution Function F(x)', fontsize=14, pad=15)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('F(x)', fontsize=12)
ax.set_xlim(0, 5)
ax.set_ylim(-0.05, 1.1)
ax.grid(True, linestyle='--', alpha=0.6)

# Legend
ax.legend(loc='upper left', frameon=True, facecolor='white', framealpha=0.9, fontsize=11)

plt.tight_layout()

# Save plot image to file instead of using plt.show()
output_filename = 'cdf_plot.png'
plt.savefig(output_filename)
plt.close()

# Open file with default viewer using subprocess based on platform
if sys.platform.startswith('darwin'):        # macOS
    subprocess.run(['open', output_filename])
elif sys.platform.startswith('win'):        # Windows
    subprocess.run(['start', output_filename], shell=True)
else:                                       # Linux/Unix
    subprocess.run(['xdg-open', output_filename])


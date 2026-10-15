import sys
import subprocess
import numpy as np
import matplotlib.pyplot as plt

# Define the PDF piecewise function P(x)
def P(x):
    return np.piecewise(
        x,
        [x < 1, (x >= 1) & (x <= 4), x > 4],
        [0, lambda x: (1 / 21) * x**2, 0]
    )

# Set figure parameters
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=150)

# Generate x values and main curve
x_full = np.linspace(0, 5, 1000)
y_full = P(x_full)
ax.plot(x_full, y_full, label=r'$P(x) = \frac{1}{21}x^2,\ 1 \leq x \leq 4$', color='#1f77b4', linewidth=2.5)

# Fill area under the curve for 2 <= x <= 3
x_fill = np.linspace(2, 3, 200)
y_fill = P(x_fill)
ax.fill_between(
    x_fill, y_fill, color='#f5a665', alpha=0.85,
    label=r'Area $P(2 \leq x \leq 3) = \frac{19}{63} \approx 0.302$'
)

# Vertical dashed lines at boundaries x = 1 and x = 4
ax.axvline(x=1, color='gray', linestyle='--', linewidth=1.2)
ax.axvline(x=4, color='gray', linestyle='--', linewidth=1.2)

# Vertical dotted red lines at fill limits x = 2 and x = 3
ax.axvline(x=2, color='#d62728', linestyle=':', linewidth=1.5)
ax.axvline(x=3, color='#d62728', linestyle=':', linewidth=1.5)

# In-graph text annotations
ax.text(0.5, 0.05, r'$P(x) = 0$', fontsize=10, color='gray', ha='center')
ax.text(0.95, 0.05, r'x = 1', fontsize=10, color='gray', ha='right')
ax.text(4.08, 0.05, r'x = 4', fontsize=10, color='gray', ha='left')
ax.text(4.6, 0.05, r'$P(x) = 0$', fontsize=10, color='gray', ha='center')

# Labels, limits, and grid formatting
ax.set_title('Probability Density Function P(x)', fontsize=14, pad=15)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('P(x)', fontsize=12)
ax.set_xlim(0, 5)
ax.set_ylim(0, 0.85)
ax.grid(True, linestyle='--', alpha=0.6)

# Legend
ax.legend(loc='upper left', frameon=True, facecolor='white', framealpha=0.9, fontsize=11)

plt.tight_layout()

# Save the figure to file
output_file = 'pdf_plot.png'
plt.savefig(output_file)
plt.close()

# Open the image file using subprocess based on operating system
if sys.platform.startswith('darwin'):        # macOS
    subprocess.run(['open', output_file])
elif sys.platform.startswith('win'):        # Windows
    subprocess.run(['start', output_file], shell=True)
else:                                       # Linux/Unix
    subprocess.run(['xdg-open', output_file])


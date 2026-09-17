import matplotlib.pyplot as plt
import numpy as np

# Take value of k as input from user
k_input = input("Enter the value of k: ")
k = float(k_input)

# Define x values range
x = np.linspace(-5, 5, 400)

# Express equations in slope-intercept form (y = mx + c)
# Equation 1: 2x + 3y = 6  =>  y = (6 - 2x) / 3
# Equation 2: 4x + 6y = 3k =>  y = (3k - 4x) / 6
y1 = (6 - 2 * x) / 3
y2 = (3 * k - 4 * x) / 6

# Plot the lines
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r"$2x + 3y = 6$", color="blue", linewidth=2.5)
plt.plot(
    x,
    y2,
    label=f"$4x + 6y = {3*k:g}$ (k={k:g})",
    color="orange",
    linestyle="--",
    linewidth=2,
)

# Graph styling
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True, linestyle=":", alpha=0.6)
plt.xlabel("x")
plt.ylabel("y")

# Dynamic title based on k
if np.isclose(k, 4):
    plt.title(
        f"k = {k:g}: Lines Overlap (Coincident - Infinitely Many Solutions)"
    )
else:
    plt.title(f"k = {k:g}: Lines are Parallel (No Solution)")

plt.legend()

# Save the figure to a file and release memory instead of calling plt.show()
plt.savefig("bt34a.png", bbox_inches="tight", dpi=300)
plt.close()


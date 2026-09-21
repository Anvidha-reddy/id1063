import math
import os
import platform
import subprocess
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# 1. Theoretical Calculation & Terminal Output
# ---------------------------------------------------------
tau = 40.0  # Time constant in seconds
target_fraction = 0.95  # 95% steady-state target

# Derivation: 0.95 = 1 - exp(-t / tau) => t = -tau * ln(1 - 0.95)
t_theoretical = -tau * math.log(1.0 - target_fraction)
t_rounded = round(t_theoretical)

print("=" * 45)
print(f"Theoretical Exact Value : {t_theoretical:.6f} seconds")
print(f"Rounded GATE Answer     : {t_rounded} seconds")
print("=" * 45)

# ---------------------------------------------------------
# 2. Graph Generation (Saved directly to PDF)
# ---------------------------------------------------------
t = np.linspace(0, 200, 500)
y = 1 - np.exp(-t / tau)

plt.figure(figsize=(8, 5))
plt.plot(
    t,
    y,
    label=r"Response $y(t) = 1 - e^{-t/40}$",
    color="#1f77b4",
    linewidth=2,
)

# Reference Grid Lines
plt.axhline(
    y=target_fraction,
    color="gray",
    linestyle="--",
    alpha=0.7,
    label="95% Steady-State Output",
)
plt.axvline(
    x=t_theoretical,
    color="gray",
    linestyle="--",
    alpha=0.7,
    label=f"Time t = {t_rounded} s",
)

# Circle and Highlight Target Point
plt.plot(
    t_theoretical,
    target_fraction,
    "o",
    ms=14,
    markerfacecolor="none",
    markeredgecolor="red",
    markeredgewidth=2.5,
    label=f"Target Value ({t_rounded} s, {target_fraction})",
)
plt.plot(t_theoretical, target_fraction, "ro", ms=5)

# Annotation
plt.annotate(
    f"({t_rounded} s, {target_fraction})",
    xy=(t_theoretical, target_fraction),
    xytext=(t_theoretical - 38, target_fraction - 0.12),
    arrowprops=dict(
        facecolor="red", shrink=0.08, width=1.5, headwidth=8
    ),
    fontsize=11,
    fontweight="bold",
    color="red",
)

plt.title(
    r"First-Order System Step Response ($\tau = 40\ \mathrm{s}$)",
    fontsize=13,
    pad=12,
)
plt.xlabel("Time $t$ (seconds)", fontsize=11)
plt.ylabel(r"Normalized Output $y(t) / y_{ss}$", fontsize=11)
plt.ylim(0, 1.05)
plt.xlim(0, 200)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="lower right", fontsize=10)

plt.tight_layout()

# Save directly to PDF file
pdf_filename = "first_order_response.pdf"
plt.savefig(pdf_filename, format="pdf", dpi=300)
plt.close()  # Closes plot buffer without calling plt.show()

# ---------------------------------------------------------
# 3. Automatically Open PDF in System Viewer
# ---------------------------------------------------------
if platform.system() == "Windows":
    os.startfile(pdf_filename)
elif platform.system() == "Darwin":  # macOS
    subprocess.run(["open", pdf_filename])
else:  # Linux / Unix
    subprocess.run(["xdg-open", pdf_filename])


#Code by Anvidha
#21-09-26

import os
import platform
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# ---------------------------------------------------------
# 1. Theoretical Verification using SymPy
# ---------------------------------------------------------
x, a, b = sp.symbols('x a b')

f_left = a + b * x
f_right = sp.sin(2 * x)

# Continuity: Left limit == Right limit at x = 0
lim_left = sp.limit(f_left, x, 0, dir='-')
lim_right = sp.limit(f_right, x, 0, dir='+')
a_val = sp.solve(sp.Eq(lim_left, lim_right), a)[0]

# Differentiability: Left derivative == Right derivative at x = 0
deriv_left = sp.limit(sp.diff(f_left, x), x, 0, dir='-')
deriv_right = sp.limit(sp.diff(f_right, x), x, 0, dir='+')
b_val = sp.solve(sp.Eq(deriv_left, deriv_right), b)[0]

ans = a_val + b_val

print("=" * 35)
print(f"Calculated Value of a : {a_val}")
print(f"Calculated Value of b : {b_val}")
print(f"Final Answer (a + b)  : {ans}")
print("=" * 35)

# ---------------------------------------------------------
# 2. Plotting and Saving directly to PDF
# ---------------------------------------------------------
a_num, b_num = float(a_val), float(b_val)

x_left = np.linspace(-1, 0, 200)
x_right = np.linspace(0, 1, 200)

y_left = a_num + b_num * x_left
y_right = np.sin(2 * x_right)

plt.figure(figsize=(7, 4.5))
plt.plot(
    x_left,
    y_left,
    'b-',
    label=r'$f(x) = 2x \quad (x \le 0)$',
    linewidth=2,
)
plt.plot(
    x_right,
    y_right,
    'g-',
    label=r'$f(x) = \sin(2x) \quad (x > 0)$',
    linewidth=2,
)
plt.plot(0, 0, 'ro', ms=8, label=r'Smooth Junction at $x=0$')

plt.title(
    r'Differentiable Piecewise Function $f(x)$ at $x=0$', fontsize=12
)
plt.xlabel('$x$', fontsize=11)
plt.ylabel('$f(x)$', fontsize=11)
plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.axvline(0, color='black', linewidth=0.8, linestyle=':')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', fontsize=10)

plt.tight_layout()

# Save directly to PDF
pdf_filename = 'q46_plot.pdf'
plt.savefig(pdf_filename, format='pdf', dpi=300)
plt.close()

# ---------------------------------------------------------
# 3. Open PDF automatically
# ---------------------------------------------------------
if platform.system() == 'Windows':
    os.startfile(pdf_filename)
elif platform.system() == 'Darwin':  # macOS
    subprocess.run(['open', pdf_filename])
else:  # Linux / Unix
    subprocess.run(['xdg-open', pdf_filename])


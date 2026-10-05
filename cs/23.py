import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import subprocess

# Take k from user
k = float(input("Enter k: "))

# ------------------------------------------------
# GENERAL MATRIX
# ------------------------------------------------

k_symbol = sp.symbols('k')

A_general = sp.Matrix([
    [1, k_symbol, 1],
    [k_symbol, 1, -1]
])

print("\nGeneral augmented matrix:")
sp.pprint(A_general)

# R2 -> R2 - kR1
R2 = A_general.row(1) - k_symbol * A_general.row(0)
A_reduced_general = sp.Matrix.vstack(
    A_general.row(0),
    R2
)

print("\nAfter R2 -> R2 - kR1:")
sp.pprint(A_reduced_general)

# ------------------------------------------------
# MATRIX FOR ENTERED k
# ------------------------------------------------

A = sp.Matrix([
    [1, k, 1],
    [k, 1, -1]
])

print("\nAugmented matrix for k =", k)
sp.pprint(A)

print("\nRREF:")
RREF = A.rref()[0]
sp.pprint(RREF)

# ------------------------------------------------
# DETERMINE NATURE OF SOLUTION
# ------------------------------------------------

if abs(1 - k**2) > 1e-10:
    print("\nUnique solution")

    solution = sp.solve([
        sp.Eq(sp.Symbol('x') + k * sp.Symbol('y'), 1),
        sp.Eq(k * sp.Symbol('x') + sp.Symbol('y'), -1)
    ], [sp.Symbol('x'), sp.Symbol('y')])

    print("Solution:")
    print(solution)

elif abs(k - 1) < 1e-10:
    print("\nNo solution")

else:
    print("\nInfinitely many solutions")


# ------------------------------------------------
# GRAPH
# ------------------------------------------------

x = np.linspace(-5, 5, 500)

# x + ky = 1
# y = (1-x)/k
#
# If k = 0, equation becomes x = 1

plt.figure(figsize=(7, 6))

if abs(k) > 1e-10:
    y1 = (1 - x) / k
    plt.plot(x, y1, label='x + ky = 1')
else:
    plt.axvline(1, label='x + ky = 1')

# kx + y = -1
# y = -1-kx

y2 = -1 - k * x
plt.plot(x, y2, label='kx + y = -1')

plt.axhline(0)
plt.axvline(0)

plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Graphs for k = {k}')
plt.grid()
plt.legend()

filename = 'matrix_graph.png'
plt.savefig(filename, dpi=150)
plt.close()

# Open graph directly in Termux
subprocess.run(['termux-open', filename])

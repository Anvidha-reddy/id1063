import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import subprocess

print("For the system:")
print("       x + ky = 1")
print("      kx +  y = -1")
print()
print("Choose k according to the case you want:")
print("  k =  0  -> Unique solution")
print("  k =  1  -> No solution")
print("  k = -1  -> Infinitely many solutions")
print("  Any other k -> Unique solution")
print()

k = float(input("Enter the value of k: "))

# ----------------------------------------
# SYMBOLIC ROW TRANSFORMATION
# ----------------------------------------

k_symbol = sp.symbols('k')

A_general = sp.Matrix([
    [1, k_symbol, 1],
    [k_symbol, 1, -1]
])

print("\nGENERAL AUGMENTED MATRIX")
sp.pprint(A_general)

R2 = A_general.row(1) - k_symbol * A_general.row(0)

A_reduced_general = sp.Matrix.vstack(
    A_general.row(0),
    R2
)

print("\nAfter row operation:")
print("R2 -> R2 - kR1")
sp.pprint(A_reduced_general)

# ----------------------------------------
# NUMERICAL MATRIX
# ----------------------------------------

A = sp.Matrix([
    [1, k],
    [k, 1]
])

Aug = sp.Matrix([
    [1, k, 1],
    [k, 1, -1]
])

print("FOR k =", k)

print("\nCoefficient matrix A:")
sp.pprint(A)

print("\nAugmented matrix [A|b]:")
sp.pprint(Aug)

# ----------------------------------------
# RANK
# ----------------------------------------

rank_A = A.rank()
rank_Aug = Aug.rank()

print("\nRank of coefficient matrix A =", rank_A)
print("Rank of augmented matrix [A|b] =", rank_Aug)

# ----------------------------------------
# RREF
# ----------------------------------------

print("\nRREF of augmented matrix:")
RREF = Aug.rref()[0]
sp.pprint(RREF)

# ----------------------------------------
# NATURE OF SOLUTION
# ----------------------------------------

if rank_A == rank_Aug == 2:
    print("\nNature of solution: UNIQUE SOLUTION")

    solution = sp.linsolve(
        (A, sp.Matrix([1, -1]))
    )

    print("Solution:")
    print(solution)

elif rank_A < rank_Aug:
    print("\nNature of solution: NO SOLUTION")

else:
    print("\nNature of solution: INFINITELY MANY SOLUTIONS")

# ----------------------------------------
# GRAPH
# ----------------------------------------

x = np.linspace(-5, 5, 500)

plt.figure(figsize=(7, 6))

if abs(k) > 1e-10:
    y1 = (1 - x) / k
    plt.plot(x, y1, label='x + ky = 1')
else:
    # k = 0 -> x = 1
    plt.axvline(1, label='x + ky = 1')

# kx + y = -1
y2 = -1 - k * x
plt.plot(x, y2, label='kx + y = -1')

plt.axhline(0)
plt.axvline(0)

plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Graphs for k = {k}")

plt.grid()
plt.legend()

filename = "matrix_graph.png"
plt.savefig(filename, dpi=150)
plt.close()


# Open graph directly in Termux
subprocess.run(["termux-open", filename])

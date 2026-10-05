import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import subprocess

print("System:")
print("       x + ky = 1")
print("      kx +  y = -1")
print()
print("Choose k:")
print("  k =  0  -> Unique solution")
print("  k =  1  -> No solution")
print("  k = -1  -> Infinitely many solutions")
print("  Any other k -> Unique solution")
print()

k = float(input("Enter the value of k: "))

# ========================================
# AUGMENTED MATRIX
# ========================================

A = sp.Matrix([
    [1, k],
    [k, 1]
])

b = sp.Matrix([
    [1],
    [-1]
])

Aug = A.row_join(b)


print("AUGMENTED MATRIX")

sp.pprint(Aug)

# ========================================
# ROW REDUCTION USING BUILT-IN RREF
# ========================================

RREF, pivots = Aug.rref()

print("ROW REDUCED ECHELON FORM (RREF)")
print("========================================")
sp.pprint(RREF)

print("\nPivot columns:", pivots)

# ========================================
# RANK USING BUILT-IN FUNCTION
# ========================================

rank_A = A.rank()
rank_Aug = Aug.rank()

print("\n========================================")
print("RANK")
print("========================================")

print("Rank(A)       =", rank_A)
print("Rank([A | b]) =", rank_Aug)

# ========================================
# NATURE OF SOLUTION
# ========================================

print("\n========================================")
print("NATURE OF SOLUTION")
print("========================================")

if rank_A == rank_Aug == 2:
    print("Unique solution")

    solution = A.inv() * b
    print("\nx =", solution[0])
    print("y =", solution[1])

elif rank_A < rank_Aug:
    print("No solution")

else:
    print("Infinitely many solutions")

# ========================================
# GRAPH
# ========================================

x = np.linspace(-5, 5, 500)

plt.figure(figsize=(7, 6))

# x + ky = 1
if abs(k) < 1e-10:
    plt.axvline(1, label="x + ky = 1")
else:
    y1 = (1 - x) / k
    plt.plot(x, y1, label="x + ky = 1")

# kx + y = -1
y2 = -1 - k * x
plt.plot(x, y2, label="kx + y = -1")

plt.axhline(0)
plt.axvline(0)

plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Graphs for k = {k}")

plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.grid()
plt.legend()

filename = "matrix_graph.png"
plt.savefig(filename, dpi=150)
plt.close()


subprocess.run(["termux-open", filename])

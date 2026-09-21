import numpy as np
import scipy.linalg as la

# Coefficient matrix A (4 atomic balance equations, 6 variables)
A = np.array([
    [6.0, 0.0, 0.0, -1.0, -1.0, 0.0],  # Carbon (C)
    [0.0, 3.0, 0.0, -0.2, 0.0, 0.0],  # Nitrogen (N)
    [12.0, 3.0, 0.0, -1.8, 0.0, -2.0],  # Hydrogen (H)
    [6.0, 0.0, 2.0, -0.5, -2.0, -1.0],  # Oxygen (O)
])

# Compute the nullspace basis vectors
null_basis = la.null_space(A)


print("Matrix Nullspace Basis Vectors (Dimension = 2):")

print(null_basis)

# Expressing in terms of x1 and x4
print("\nParametric Form:")
print("x5 (CO2) = 6*x1 - x4")
print("x2 (NH3) = (1/15)*x4")
print("x6 (H2O) = 6*x1 - 0.8*x4")
print("x3 (O2)  = 3*x1 - 1.15*x4")



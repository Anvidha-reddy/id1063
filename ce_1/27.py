import numpy as np
from scipy.linalg import cholesky

# 1. Define Matrix A
A = np.array([
    [9, 15],
    [15, 50]
], dtype=float)

# 2. Perform Cholesky Decomposition (A = L @ L.T)
# scipy.linalg.cholesky returns Upper Triangular by default, so lower=True gives L
L = cholesky(A, lower=True)

# 3. Extract l_22 element
l_22 = L[1, 1]
abs_l_22 = abs(l_22)

# Print results
print("Lower Triangular Matrix L:")
print(L)
print(f"\n|l_22| = {int(abs_l_22)}")


import numpy as np

# Define Matrix P
P = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
], dtype=float)

# --- Option A Verification ---
trace_P = np.trace(P)
eigenvalues = np.linalg.eigvals(P)
sum_eigenvalues = np.sum(eigenvalues)
is_option_A_true = np.isclose(trace_P, sum_eigenvalues)

# --- Option B Verification ---
P_transpose_P = P.T @ P
identity_matrix = np.eye(3)
is_option_B_true = np.allclose(P_transpose_P, identity_matrix)

# --- Option C Verification ---
is_option_C_true = np.allclose(P.T, -P)

# --- Option D Verification ---
abs_eigenvalues = np.abs(eigenvalues)
is_option_D_true = np.allclose(abs_eigenvalues, 1.0)

# Print Verification Results
print(f"Eigenvalues of P: {eigenvalues}")
print(f"Option A (Trace == Sum of Eigenvalues): {is_option_A_true} (Trace = {trace_P}, Sum = {sum_eigenvalues})")
print(f"Option B (P^T * P is Identity): {is_option_B_true}")
print(f"Option C (P is Skew-Symmetric): {is_option_C_true}")
print(f"Option D (|lambda| == 1 for all lambda): {is_option_D_true} (Magnitudes = {abs_eigenvalues})")


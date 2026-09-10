import sympy as sp

# 1. Define the symbolic variable k
k = sp.Symbol('k')

# 2. Define the Augmented Matrix [A|B]
#    2x + 3y = 6
#    4x + 6y = 3k
M = sp.Matrix([
    [2, 3, 6],
    [4, 6, 3*k]
])

# 3. Perform Row Operations (R2 = R2 - 2*R1) to reach Row Echelon Form
M_echelon = M.copy()
M_echelon[1, :] = M_echelon[1, :] - 2 * M_echelon[0, :]

print("Row Echelon Form Matrix:")
sp.pprint(M_echelon)

# 4. Extract the bottom-right term (3*k - 12) and set it to 0
consistency_condition = M_echelon[1, 2]

# 5. Solve for k
k_value = sp.solve(consistency_condition, k)[0]

print(f"\nCondition for consistency: {consistency_condition} = 0")
print(f"Value of k: {k_value}")


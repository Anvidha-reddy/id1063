import sympy as sp

# 1. Define symbolic variables
x, y, z = sp.symbols('x y z', real=True)

# 2. Define the implicit surface function f(x, y, z) = 0
f = 2*x**2 - y**2 - z**2

# 3. Calculate the gradient vector (del f)
grad_f = [sp.diff(f, x), sp.diff(f, y), sp.diff(f, z)]
print("Gradient vector field grad(f):", grad_f)

# 4. Evaluate gradient at point P(1, 0, sqrt(2))
point = {x: 1, y: 0, z: sp.sqrt(2)}
grad_at_P = [comp.subs(point) for comp in grad_f]
print("Gradient vector at P:", grad_at_P)

# 5. Calculate magnitude of the gradient vector at P
magnitude = sp.sqrt(sum([comp**2 for comp in grad_at_P]))
print("Magnitude of gradient vector:", magnitude)

# 6. Calculate the unit normal vector
unit_normal = [sp.simplify(comp / magnitude) for comp in grad_at_P]
print("Unit normal vector components (i, j, k):", unit_normal)

# 7. Verify match with Option (D): (sqrt(2)/sqrt(3))*i - (1/sqrt(3))*k
option_d = [sp.sqrt(2)/sp.sqrt(3), 0, -1/sp.sqrt(3)]
print("Matches Option D exactly:", unit_normal == option_d)


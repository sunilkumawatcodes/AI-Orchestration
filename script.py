import sympy as sp

x = sp.symbols('x')
lhs = 2 + 2 + x
rhs = 4 + x

print("Left side :", lhs)
print("Right side:", rhs)
print("Simplified difference (lhs - rhs):", sp.simplify(lhs - rhs))
print("Is it an identity (true for ALL x)?", sp.simplify(lhs - rhs) == 0)

# Try a few sample values
for val in [0, 7, -100, 3.5]:
    print(f"  ? = {val:>6} -> {lhs.subs(x,val)} = {rhs.subs(x,val)} ? {lhs.subs(x,val) == rhs.subs(x,val)}")
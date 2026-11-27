"""Solving a 3*3 linear system using the Gauss_Jacobi iterative method."""
# Gauss-Jacobi method for linear equations:
# 27x + 6y - z = 85
# 6x + 15y + 2z = 72
# x + y + 54z = 110

# Initial values
x = 0.0
y = 0.0
z = 0.0

# Check diagonal dominance
if 27 > (6 + 1) and 15 > (6 + 2) and 54 > (1 + 1):
    print("System is diagonally dominant. Convergence is guaranteed.")
else:
    print("Warning: System may not be diagonally dominant.")

print("-" * 55)
print("Iter   x          y          z")
print("-" * 55)

# Run up to 20 iterations
for step in range(1, 21):
    # Calculate new values using previous x, y, z
    new_x = (85 - 6 * y + z) / 27
    new_y = (72 - 6 * x - 2 * z) / 15
    new_z = (110 - x - y) / 54

    print(step, round(new_x, 4), round(new_y, 4), round(new_z, 4))

    # Stop when change is smaller than 0.0001 (for 3 decimal places)
    if abs(new_x - x) < 0.0001 and abs(new_y - y) < 0.0001 and abs(new_z - z) < 0.0001:
        x = new_x
        y = new_y
        z = new_z
        break

    # Update x, y, z for the next step
    x = new_x
    y = new_y
    z = new_z

print("-" * 55)
print("Answer (up to 3 decimal places):")
print("x =", round(x, 3))
print("y =", round(y, 3))
print("z =", round(z, 3))
"""
Program: Find the roots of a quadratic
"""

a = eval(input("Enter a"))
b = eval(input("Enter b"))
c = eval(input("Enter c"))

x1 = (-(b)+(b ** 2 - 4 * a * c))/2 * a
x2 = (-(b)-(b ** 2 - 4 * a * c))/2 * a

print("first root: ", x1)
print("second root: ", x2)
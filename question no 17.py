a=float(input("Enter number a"))
b=float(input("Enter number b"))
c=float(input("Enter number c"))
d = b**2 - 4*a*c
if d == 0:
    root = -b / (2*a)
    print("You have one root")
elif d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("You have 2 roots:", root1, "and", root2)

else:
    print("No real roots")
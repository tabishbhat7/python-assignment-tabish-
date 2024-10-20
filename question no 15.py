a = (input("Enter the first side (a)"))
b = (input("Enter the second side (b)"))
c = (input("Enter the third side (c)"))
if a + b > c and a + c > b and b + c > a:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
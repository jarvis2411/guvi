a = int(input("Enter the first side:"))
b = int(input("Enter the second side:"))
c = int(input("Enter the third side:"))
if a+b > c and a+c > b and b+c > a:
    print("It is a valid triangle")
else:
    print("It is a invalid triangle")

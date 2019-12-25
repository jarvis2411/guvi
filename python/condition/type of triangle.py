a = int(input("Enter the first side:"))
b = int(input("Enter the second side:"))
c = int(input("Enter the third side:"))
if a+b > c and a+c > b and b+c > a:
    if a == b == c:
        print("It is a Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("It is an Isoceles Triangle")
    else:
        print("It is a Scalene Triangle")
else:
    print("It is a invalid triangle")

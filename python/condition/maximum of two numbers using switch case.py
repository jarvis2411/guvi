a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = a - b
if c > 0:
    print(a,"is greater than",b)
elif c == 0:
    print(a,"is equal to",b)
elif c < 0:
    print(b,"is greater than",a)
else:
    print("Invalid input")

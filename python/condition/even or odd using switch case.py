a = int(input("Enter the number:"))
b = a / 2
c = a // 2
if b == c:
    print(a,"is even")
elif b > c:
    print(a,"is odd")
else:
    print("Invalid input")

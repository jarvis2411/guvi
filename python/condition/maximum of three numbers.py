a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a>b:
    if a>c:
        print(a,"is greatest of all")
    else:
        print(c,"is greatest of all")
else:
    if b>c:
        print(b,"is greatest of all")
    else:
        print(c,"is greatest of all")

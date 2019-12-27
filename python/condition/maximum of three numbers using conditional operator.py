a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
print(a,"is greatest of all") if a>b and a>c else print(c,"is greatest of all") if a>b and a<c else print(b,"is greatest of all")   if b>c else print(c,"is greatest of all")

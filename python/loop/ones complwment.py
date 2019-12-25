n = input("Enter the binary number:")
a = []
b = len(n)
c = 0
for i in range(0,b):
    if n[i] == '1':
        a.append(0)
    elif n[i] == '0':
        a.append(1)
    else:
        print("Invalid input!!")
print("The one's complement of",n,"is")
for i in range(0,b):
    print(a[i],end="")

n = input("Enter the binary number:")
a = []
d = []
b = len(n)
c = 1
for i in range(0,b):
    if n[i] == '1':
        a.append(0)
    elif n[i] == '0':
        a.append(1)
    else:
        print("Invalid input!!")
print("The two's complement of",n,"is")
for i in range(b-1,-1,-1):
    if c == 1 and a[i] == 1:
        d.append(0)
    elif c == 1 and a[i] == 0:
        d.append(1)
        c = 0
    else:
        d.append(a[i])
for i in range(b-1,-1,-1):
    print(d[i],end="")  

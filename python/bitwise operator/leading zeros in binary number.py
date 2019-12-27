n = input("Enter a binary number:")
c = 0
m = len(n)
for i in range(0,m):
    if int(n[i]) == 0:
        c = c + 1
    elif int(n[i]) == 1:
        break
    else:
        c = c
print("The number of leading zeros in",n,"is",c)

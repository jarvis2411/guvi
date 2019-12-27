n = input("Enter a binary number:")
c = 0
d = 0
m = len(n)
for i in range(0,m):
    if int(n[i]) == 0:
        c = c + 1
    else:
        d = d + 1
print("The number of zeros in",n,"is",c)
print("The number of ones in",n,"is",d)

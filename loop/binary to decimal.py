n = input("Enter the binary number:")
a = len(n)
d = 0
j = 0
for i in range(a-1,-1,-1):
    d += (int(n[i]) *(2**j))
    j += 1
print("The decimal number for",n,"is",d)

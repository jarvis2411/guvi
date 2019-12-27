n = int(input("Enter the number:"))
o = n
d,j = 0,0
p = []
while n>0:
    p.append(n%2)
    n = n//2
m = len(p)
a = int(input("Enter the number to set the nth bit:"))
if a<= m:
    p[-a] = 0
    for i in range(0,m):
        d += (int(p[i]) *(2**j))
        j += 1
    print("The number after changing the bit",0,"is",d)
else:
    print("Invalid bit size")

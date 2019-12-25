n = int(input("Enter the number:"))
o = n
p = []
while n>0:
    p.append(n%2)
    n = n//2
m = len(p)
print("The binary number of",o,"is",end = " ")
for i in range(m-1,-1,-1):
    print(p[i],end = "")
    

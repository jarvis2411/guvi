n = int(input("Enter the base:"))
p = int(input("Enter the power:"))
q = 1
for i in range(1,p+1):
    q = q * n
print(n,"^",p,"=",q)

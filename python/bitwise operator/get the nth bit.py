n = int(input("Enter the number:"))
o = n
p = []
while n>0:
    p.append(n%2)
    n = n//2
m = len(p)
a = int(input("Enter the number to get the nth bit:"))
if a<= m:
    print("The",a,"th bit of",o,"is",p[-a])
else:
    print("Invalid bit size")

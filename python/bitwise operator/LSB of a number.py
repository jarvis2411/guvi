n = int(input("Enter the number to check LSB:"))
o = n
p = []
while n>0:
    p.append(n%2)
    n = n//2
if int(p[0])&1:
    print("The LSB of",o,"is 1")
else:
    print("The LSB of",o,"is 0")

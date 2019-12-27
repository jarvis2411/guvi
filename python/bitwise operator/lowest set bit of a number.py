n = int(input("Enter the number:"))
o = n
p = []
while n>0:
    p.append(n%2)
    n = n//2
m = len(p)
for i in range(0,m):
    if p[i] == 1:
        print("The highest set bit of ",o,"is", i+1)
        break
    elif 1 not in p:
        print("There is no set bit")
    else:
        continue

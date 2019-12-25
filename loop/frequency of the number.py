n = int(input("Enter the number:"))
m = n
a,b = [ ],[ ]
count = 0
while n>0:
    a.append(n%10)
    n = n//10
c = len(a)
for i in range(0,c):
    d = a[i]
    count = 0
    for j in range(0,c):
        if d == a[j]:
            count += 1
    b.append(count)
for i in range(0,c):
    print("The frequency of",a[i],"in",m,"is",b[i])

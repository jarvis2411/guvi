a = [ ]
b = int(input("Enter the list range:"))
for i in range(0,b):
    c = int(input("Enter the list element:"))
    a.append(c)
d,e=0,0
print("The list is",a)
for i in range(0,b):
    if a[i] == 7:
        d += 1
        print("7 is present at " ,i)
    elif a[i] == 2:
        print("2 is present at " ,i)
        e += 1
print("7 comes",d,"times")
print("2 comes",e,"times")


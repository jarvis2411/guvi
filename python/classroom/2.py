a = [ ]
b = int(input("Enter the list range:"))
for i in range(0,b):
    c = int(input("Enter the list element:"))
    a.append(c)    
for i in range(0,b):
    d = 0
    for j in range(2,(a[i]//2)+1):
        if(a[i]%j == 0):
            d += 1
    if d== 0:
        print(a[i],"is a prime number")
    else:
        print(a[i],"is not a prime number")    

n = int(input("Enter the range:"))
a,b,c = 0,1,0
print("The fibonacci series from 1 to",n,":")
print(a)
print(b)
for i in range(2,n):
    c = a+b
    print(c)
    a,b = b,c
    

n = int(input("Enter the number:"))
print("The number of digits in",n,"is",len(str(n))) #using in-built function
m = n
c = 0
while n> 0:
    n = n//10
    c += 1
print("The number of digits in",m,"is",c) #using normal method

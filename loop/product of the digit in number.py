n = int(input("Enter the number:"))
m = n
c = 1
while n> 0:
    c *= n%10
    n = n//10    
print("The product of digit in",m,"is",c)

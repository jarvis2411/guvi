n = int(input("Enter the number:"))
m = n
c = 0
while n> 0:
    c = c*10 + n%10
    n = n//10    
print("The reverse of number in",m,"is",c)

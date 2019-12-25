n = int(input("Enter the number:"))
m = n
c = 0
while n> 0:
    c += n%10
    n = n//10    
print("The sum of digit in",m,"is",c)

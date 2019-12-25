n = int(input("Enter the number:"))
m = n
c = 0
while n> 0:
    n = n//10
    c += 1
d = c - 1    
print("The last digit of",m,"is",m%10)
print("The first digit of",m,"is",m//(10**d))

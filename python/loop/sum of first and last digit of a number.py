n = int(input("Enter the number:"))
m = n
c = 0
while n> 0:
    n = n//10
    c += 1
d = c - 1    
e =((m % 10) + (m // (10 ** d)))
print("The sum of first digit=",(m // (10 ** d)),"and the last digit=",m % 10,"is",e)

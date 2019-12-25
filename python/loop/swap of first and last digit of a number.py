n = int(input("Enter the number:"))
m = n
o = n
c = 0
while n> 0:
    n = n//10
    c += 1
d = c - 1    
a = m % 10
b = m // (10 ** d)
m = m - (b*(10**d)) - a
m = m + (a*(10**d)) +b
print("The first and last digit of the number ",o,"is swapped as",m)



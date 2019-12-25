n = int(input("Enter the number to be checked:"))
m = (n//2)+1
c = 0
for i in range(2,m):
    if n%i == 0:
        c = 1
if c == 0:
    print("The number",n,"is prime")
else:
    print("The number",n,"is not prime")

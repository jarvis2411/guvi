n = int(input("Enter the range:"))
sum = 0
for i in range(1,n+1):
    m = (i//2)+1
    c = 0
    for b in range(2,m):
        if i%b == 0:
            c = 1
    if c == 0:
        sum += i
print("The sum of prime numbers from 1 to",n,"is",sum)

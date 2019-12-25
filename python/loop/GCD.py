m = int(input("1st number:"))
n = int(input("2st number:"))
N = 0
M = 0
if m > n:
    N = n
else:
    N = m
for i in range(1,N+1):
    if m%i == 0 and n %i  == 0:
        M = i
print("The GCD of",m,"and",n,"is",M)        

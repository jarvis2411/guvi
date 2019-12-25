n = int(input("Enter the number:"))
sum = 0
for i in range(1,n):
    if n%i == 0:
        sum += i       
if sum == n:
    print(n,"is a Perfect number")
else:
    print(n,"is not a Perfect number")

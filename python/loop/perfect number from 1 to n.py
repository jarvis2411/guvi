n = int(input("Enter the range:"))
for j in range(1,n+1):
    sum = 0
    for i in range(1,j):
        if j%i == 0:
            sum += i       
    if sum == j:
        print(j,"is a Perfect number")
    else:
        continue

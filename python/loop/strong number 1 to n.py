m = int(input("Enter the range:"))
for i in range(1,m+1):
    q = i
    sum = 0
    while i>0:
        fact = 1
        n = i%10
        for j in range(1,n+1):
            fact = fact * j
        sum += fact
        i = i//10
    if q == sum:
        print(q,"is a strong number")
    else:
        continue
    

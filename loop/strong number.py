m = int(input("Enter the number:"))
q = m
sum = 0
while m>0:
    fact = 1
    n = m%10
    for i in range(1,n+1):
        fact = fact * i
    sum += fact
    m = m//10
if q == sum:
    print(q,"is a strong number")
else:
    print(q,"is not a strong number")
    

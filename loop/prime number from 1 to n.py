n = int(input("Enter the range:"))
for i in range(1,n+1):
    m = (i//2)+1
    c = 0
    for b in range(2,m):
        if i%b == 0:
            c = 1
    if c == 0:
        print("The number",i,"is prime")
    else:
        print("The number",i,"is not prime")

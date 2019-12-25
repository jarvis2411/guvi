n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    a = 1
    for j in range(1,i+1):
        print(a,end = " ")
        a = a*(i-j)//j
    print("\n")

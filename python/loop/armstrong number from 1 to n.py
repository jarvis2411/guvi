n = int(input("Enter the range of numbers to be checked:"))
for i in range(1,n+1):
    m = 0
    p = i
    while i>0:
        m += ((i%10)**3)
        i = i//10
    if m == p:
        print("The number",p,"is a Armstrong Number")
    else:
        continue

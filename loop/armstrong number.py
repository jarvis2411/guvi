n = int(input("Enter the number to be checked:"))
m = 0
p = n
while n>0:
    m += ((n%10)**3)
    n = n//10
if m == p:
    print("The number",p,"is a Armstrong Number")
else:
    print("The number",p,"is not an Armstrong Number")

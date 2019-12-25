n = int(input("Enter the month number:"))
a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
c = 2
if n in a:
    print("The total number of days in month",n,"is 31")
elif n in b:
    print("The total number of days in month",n,"is 30")
elif n == c:
    print("This month may have 28 or 29 days based on leap year")
else:
    print("Invalid month number")

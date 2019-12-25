a = int(input("Enter the year:"))
if a%4 == 0 and a%400 == 0 :
    print(a,"is leap year")
else:
    print(a,"is not a leap year")

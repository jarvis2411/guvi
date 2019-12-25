a = int(input("Enter the number:"))
if a%5 == 0 and a%11 == 0:
    print(a,"is divisible by both 5 and 11.")
elif a %5 == 0:
    print(a," is divisible by 5")
elif a%11 == 0:
    print(a,"is divisible by 11")
else:
    print(a, "is not divisible by both 11 and 5") 

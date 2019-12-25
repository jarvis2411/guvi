a = input("Enter the character:")
if (ord(a)>64 and ord(a) < 91) or( ord(a) > 96 and ord(a) < 123):
    print(a,"is an alphabet")
elif ord(a)>47 and ord(a)<58:
    print(a,"is a digit")
else:
    print(a," is a special character")

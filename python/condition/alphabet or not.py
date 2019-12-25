a = input("Enter the character:")
if (ord(a)>64 and ord(a) < 91) or( ord(a) > 96 and ord(a) < 123):
    print(a,"is an alphabet")
else:
    print(a,"is not an alphabet")

n = input("Enter a character:")
if ord(n) > 64 and ord(n)<91:
    print(n,"is in Uppercase")
elif ord(n) > 96 and ord(n)<123:
    print(n,"is in Lowercase")
else:
    print("Invalid character")

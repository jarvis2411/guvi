a = input("Enter the string to be encrypted:")
c = int(input("Enter the key to encrypt:"))
b = []
for i in range(len(a)):
  b.append(chr(ord(a[i])+c))
print("The encrypted string is",end = " ")
for i in range(len(a)):
  print(b[i],end="")
print()
print("The decrypted string is",end = " ")
for i in range(len(a)):
  print(chr(ord(b[i])-c),end = "")

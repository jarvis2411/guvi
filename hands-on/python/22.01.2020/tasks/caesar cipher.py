a = input("Enter the string to be encrypted:")
c = int(input("Enter the key to encrypt:"))
b = []
for i in range(len(a)):
  d = ord(a[i])
  if d >64 and d < 91: 
    if d+c > 90:
      d = (d+c) - 26
    else:
      d = d + c
    b.append(chr(d))
  elif d >96 and d < 123: 
    if d+c > 122:
      d = (d+c) - 26
    else:
      d = d + c
    b.append(chr(d))
  else:
    b.append(chr(d))
print("The encrypted string is",end = " ")
for i in range(len(a)):
  print(b[i],end="")
print()
print("The decrypted string is",end = " ")
for i in range(len(a)):
  d = ord(b[i])
  if d >64 and d < 91: 
    if d-c < 65:
      d = (d-c) + 26
    else:
      d = d - c
    print(chr(d),end="")
  elif d >96 and d < 123: 
    if d-c < 97:
      d = (d-c) + 26
    else:
      d = d - c
    print(chr(d),end="")
  else:
    print(chr(d),end="")

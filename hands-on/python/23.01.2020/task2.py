size = int(input("Enter the size of the list:"))
a = []
odd = []
even = []
oddSum,evenSum = 0,0
for i in range(size):
  a.append(int(input("Enter the element:")))
for i in range(size):
  if a[i] % 2 == 0:
    evenSum += a[i]
    even.append(a[i])
  else:
    odd.append(a[i])
    oddSum += a[i]
print("The sum of odd list",odd,"is",oddSum)
print("The sum of even list",even,"is",evenSum)

a = 0
b = []
c = int(input("Enter the Size of the list:"))
for i in range(0,c):
  d = int(input("Enter the element of the list:"))
  b.append(d)
while(True):
  e = int(input("Enter the key value to add the elements:"))
  if e < c:
    for i in range(0,e+1):
      a += b[i]
    print("The sum of the",e+1,"elements is",a)
    break
  else:
    print("Please!!! Enter the key value less than the size of list")

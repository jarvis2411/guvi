print('***************Quiz Game *******************')
a = input("Enter your name:")
b = 0
print()
print("1.What is our national flower:")
c = input("1.Lotus 2.Lily 3.Rose")
if c.upper()== "LOTUS" or c == '1':
  b += 1
print()
print("2.What is our national animal:")
c = input("1.Elepant 2.Tiger 3.Lion")
if c.upper()== "TIGER" or c == '2':
  b += 1
print()
print("3.What is our national bird:")
c = input("1.Cuckoo 2.Hen 3.Peacock")
if c.upper()== "PEACOCK" or c == '3':
  b += 1
print()
print("4.What is our national game:")
c = input("1.Hockey 2.Football 3.Cricket")
if c.upper()== "HOCKEY" or c =='1':
  b += 1
print()
print("5.What is our capital:")
c = input("1.Delhi 2.Chennai 3.Mumbai")
if c.upper()== "DELHI" or c == '1':
  b += 1
print()

print("Hey",a,"your score is",b)

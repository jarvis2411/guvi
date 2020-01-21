import random

a = random.randint(0,11)
i = 5
while i>0:
  b = int(input("Enter the number:"))
  if b == a:
    print("Yeah!!! your guess is correct")
    break
  else:
    i -= 1
    print("You have",i,"chances")
if i == 0:
  print("Sorry!!! your guess is totally wrong")

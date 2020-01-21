import random 
a = ['guvi', 'water', 'board', 'geeks'] 
b = random.choice(a)
n = 12
c = []
d = 0
while (n>0):
  for i in range(len(b)):
    c.append('_')
  while (d < len(b)):
    print(' '.join(c))
    p = input()
    if p in b:
      for i in range(len(b)):
        if b[i] == p:
          c[i] = p
          d += 1
    else:
      n -= 1
      print("You have",n,"chances")
      if n == 0:
        break
  break
if n>0:
  print("Won")
else:
  print("Lose")
  

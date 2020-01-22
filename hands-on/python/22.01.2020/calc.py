def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b
c = input("1.Add 2.Sub 3.Mul 4.Div:")
c = c.upper()
if c == 'ADD':
  a = int(input("num1:"))
  b = int(input("num2:"))
  print(add(a,b))
elif c == "SUB":
  a = int(input("num1:"))
  b = int(input("num2:"))
  print(sub(a,b))
elif c == "MUL":
  a = int(input("num1:"))
  b = int(input("num2:"))
  print(mul(a,b))
elif c == "DIV":
  a = int(input("num1:"))
  b = int(input("num2:"))
  print(div(a,b))
else:
  print("Invalid option")

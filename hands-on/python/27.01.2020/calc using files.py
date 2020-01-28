def add(a,b):
  cal.write("The sum of %d and %d is %d\r\n"%(a,b,a+b))
  return a+b
def sub(a,b):
  cal.write("The subtraction of %d and %d is %d\r\n"%(a,b,a-b))
  return a-b
def mul(a,b):
  cal.write("The multiplication of %d and %d is %d\r\n"%(a,b,a*b))
  return a*b
def div(a,b):
  cal.write("The division of %d and %d is %d\r\n"%(a,b,a/b))
  return a/b
cal = open("calc.txt","a+")
c = input("1.Add 2.Sub 3.Mul 4.Div:")
cal.write("1.Add 2.Sub 3.Mul 4.Div:\r\n")
while(1):
  c = c.upper()
  if c == 'ADD' or c[0] == '1':
    while(1):
      cal.write("Your choice is addition\r\n")
      a = input("num1:")
      b = input("num2:")
      cal.write("num1:%s\r\n"%(a))
      cal.write("num2:%s\r\n"%(b))
      if a.isdigit() and b.isdigit():
        print(add(int(a),int(b)))
        break
      else:
        cal.write("Use only numbers\r\n")
        print("Use only numbers")
    break
  elif c == "SUB" or c[0] == '2':
    while(1):
      a = input("num1:")
      b = input("num2:")
      cal.write("num1:%s"%(a))
      cal.write("num2:%s"%(b))
      if a.isdigit() and b.isdigit():
        print(sub(int(a),int(b)))
        break
      else:
        print("Use only numbers")
        cal.write("Use only numbers\r\n")
    break
  elif c == "MUL" or c[0] == '3':
    while(1):
      a = input("num1:")
      b = input("num2:")
      cal.write("num1:%s\r\n"%(a))
      cal.write("num2:%s\r\n"%(b))
      if a.isdigit() and b.isdigit():
        print(mul(int(a),int(b)))
        break
      else:
        print("Use only numbers")
        cal.write("Use only numbers\r\n")
    break
  elif c == "DIV" or c[0] == '4':
    while(1):
      a = input("num1:")
      b = input("num2:")
      cal.write("num1:%s\r\n"%(a))
      cal.write("num2:%s\r\n"%(b))
      if a.isdigit() and b.isdigit():
        if b != '0' and a != '0':
          print(div(int(a),int(b)))
          break
        else:
          print("0 division not possible")
          cal.write("0 division not possible\r\n")
      else:
        print("Use only numbers")
        cal.write("Use only numbers\r\n")
    break
  else:
    print("Invalid option")
    cal.write("Invalid option \r\n")
    d = input("If you want to quit press \'q\'")
    cal.write("If you want to quit press \'q\'\r\n")    
    if d == 'q' or d == 'Q':
      cal.write("You pressed %s"%(d))
      break
    else:
      c = input("1.Add 2.Sub 3.Mul 4.Div:")
      cal.write("1.Add 2.Sub 3.Mul 4.Div:\r\n")
cal.close()

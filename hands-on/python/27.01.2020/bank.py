import random


def register():
  dic = { }
  f =  open("bank.txt","a+")
  f.seek(0)
  g = f.read()
  a = [ ]
  if len(g) == 0:
    e = { }
    while(1):
      id = random.randint(99,1000)
      if id not in e.items():
        print("Your unique id is:",id)
        while(1):
          name = input("Enter the name:")
          if name.isalpha():
            a.append(name)
            break
          else:
            print("Name should only be in alphabets")
        while(1):
          num = input("Enter the mobile number:")
          if num.isdigit():
            if len(num) == 10:
              a.append(num)
              break
            else:
              print("Mobile numbers should be 10 digits")
          else:
            print("Number should only be in numbers")
        while(1):
          emailId = input("Enter the email address:")
          if emailId.endswith('@gmail.com'):
            a.append(emailId)
            break
          else:
            print("Invalid email address")
        while(1):
          password = input("Enter the password:")
          SpecialSym =['$', '@', '#', '%'] 
          val = True
          if len(password) < 6: 
            print('length should be at least 6') 
            val = False
          if len(password) > 20: 
            print('length should be not be greater than 8') 
            val = False
          if not any(char.isdigit() for char in password): 
            print('Password should have at least one numeral') 
            val = False
          if not any(char.isupper() for char in password): 
            print('Password should have at least one uppercase letter') 
            val = False
          if not any(char.islower() for char in password): 
            print('Password should have at least one lowercase letter') 
            val = False
          if not any(char in SpecialSym for char in password): 
            print('Password should have at least one of the symbols $@#') 
            val = False
          if val: 
            a.append(password) 
            break
        while(1):
          p = [ ]
          amount = input("Enter the initial deposit:")
          if amount.isdigit():
            if int(amount) > 10000:
              p.append(int(amount))
              a.append(p)
              break
            else:
              print("Intial amount should be greater than 10000")
          else:
            print("Amount should only be in numbers")
        #g = open("bank.txt","r")
        dic[id] = a
        f.write("%s"%(dic))
        break
  else:
    while(1):
      e = eval(g)
      id = random.randint(99,1000)
      if id not in e.items():
        print("Your unique id is:",id)
        while(1):
          name = input("Enter the name:")
          if name.isalpha():
            a.append(name)
            break
          else:
            print("Name should only be in alphabets")
        while(1):
          num = input("Enter the mobile number:")
          if num.isdigit():
            if len(num) == 10:
              a.append(num)
              break
            else:
              print("Mobile numbers should be 10 digits")
          else:
            print("Number should only be in numbers")
        while(1):
          emailId = input("Enter the email address:")
          if emailId.endswith('@gmail.com'):
            a.append(emailId)
            break
          else:
            print("Invalid email address")
        while(1):
          password = input("Enter the password:")
          SpecialSym =['$', '@', '#', '%'] 
          val = True
          if len(password) < 6: 
            print('length should be at least 6') 
            val = False
          if len(password) > 20: 
            print('length should be not be greater than 8') 
            val = False
          if not any(char.isdigit() for char in password): 
            print('Password should have at least one numeral') 
            val = False
          if not any(char.isupper() for char in password): 
            print('Password should have at least one uppercase letter') 
            val = False
          if not any(char.islower() for char in password): 
            print('Password should have at least one lowercase letter') 
            val = False
          if not any(char in SpecialSym for char in password): 
            print('Password should have at least one of the symbols $@#') 
            val = False
          if val: 
            a.append(password) 
            break
        while(1):
          p = [ ]
          amount = input("Enter the initial deposit:")
          if amount.isdigit():
            if int(amount) > 10000:
              p.append(int(amount))
              a.append(p)
              break
            else:
              print("Intial amount should be greater than 10000")
          else:
            print("Amount should only be in numbers")
        f.seek(0)
        d = eval(f.read())
        d.update({id:a})
        #print(d)
        dic = d
        f.close()
        '''g = open("bank.txt","r")
        dic[id] = a
        g.write("%s"%(dic))'''
        break
  f = open("bank.txt","w+")
  f.seek(0)
  f.write("%s"%(dic))
  f.close()

  
def login():
  f = open("bank.txt","r")
  e = eval(f.read())
  while(1):
    id = input("Enter your id:")
    if id.digit():
      if id in e:
        pwd = input("Enter your password:") 
        if password == e[id][-2]:
          print("Login successfull")
          while(1):
            print("1.Balance 2.Deposit 3.Withdraw 4.Exit")
            a = input("Enter your choice:")
            a.upper()
            if a == 'BALANCE' or a == '1':
              balance(id)
            elif a == 'DEPOSIT' or a == '2':
              deposit(id)
            elif a == 'WITHDRAW' or a == '3':
              withdraw(id)
            elif a == 'EXIT' or a == '4':
              break
            else:
              print("Invalid option")
        else:
          print("Invalid password")
      else:
        print("Invalid user id..... If you are new kindly signup... or check with different user credentials")
    else:
      print("Id should be only in number")
  f.close()


def deposit(id):
  while(1):
    b = 0
    amount = input("Enter the amount to be deposited:")
    if amount.isdigit():
      if int(amount) > 4999 and int(amount) < 50000:
        amount = int(amount)
        f = open("bank.txt","a+")
        f.seek(0)
        d = eval(f.read())
        a = d[id][-1]
        for i in range(len(a)):
          b = a[i]
        a.append(amount+b)
        print("The deposited amount in",id,"is",amount)
        print("The balance after amount deposited is",amount+b)
        #d.update({id:a})
        #print(d)
        dic = d
        f.close()
        break
      else:
        print("Deposit amount should be greater than 5000 and less than 50000")
    else:
      print("Amount should only be in numbers")
  f = open("bank.txt","w+")
  f.seek(0)
  f.write("%s"%(dic))
  f.close()

def balance(id):
  f = open("bank.txt","r+")
  f = open("bank.txt","a+")
  f.seek(0)
  d = eval(f.read())
  a = d[id][-1]
  print(id,'your current balance is',a[-1])


def withdraw(id):
  b = 0
  while(1):
    amount = input("Enter the amount to be withdraw:")
    if amount.isdigit():
      amount = int(amount)
      f = open("bank.txt","a+")
      f.seek(0)
      d = eval(f.read())
      a = d[id][-1]
      b = a[-1]
      if b-amount > 10000:
        a.append(b-amount)
        print("The  amount withdrawed in",id,"is",amount)
        print("The balance after amount withdrawed is",b-amount)
        dic = d
        f.close()
        break
      else:
        print("Minimum balance should be 10000")
    else:
      print("Amount should only be in numbers")
  f = open("bank.txt","w+")
  f.seek(0)
  f.write("%s"%(dic))
  f.close()
  

while(1):
  print("1.Login 2.Register 3.Exit")
  a = input("Enter your choice:")
  a.upper()
  if a == 'LOGIN' or a == '1':
    login()
  elif a == 'REGISTER' or a == '2':
    register()
  elif a == 'EXIT' or a == '3':
    break
  else:
    print("Invalid option")
    

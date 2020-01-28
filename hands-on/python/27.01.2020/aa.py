import random
import os
m=[]
d={}
if(os.path.getsize("aa.txt")==0):
    print("file is empty")
else:
    f=open("aa.txt","r")
    d=eval(f.read())
    f.close()
print("Welcome to JK Bank\n")
print("""menu:
        1.register
        2.log in
        3.exit""")
print("\n")
choice=int(input("enter choice:"))
def register():
    f=open("aa.txt","w")
    l=[]
    print("******************Registeration page*******************")
    name=str(input("enter name:"))
    l.append(name)
    email_id=str(input("enter email_id:"))
    while(not(email_id.endswith("@gmail.com"))):
        print("enter a valid email_id:")
        email_id=str(input("email_id:"))            
    l.append(email_id)
    phone_number=str(input("phone_number:"))
    while(not(phone_number.isdigit() and (len(phone_number)==10))):
        print("enter valid phone number:")
        phone_number=str(input("phone_number:"))
    l.append(phone_number)
    password=str(input("password:"))
    while(not(len(password)>=4 and len(password)<=8)):
        print("enter a valid password:")
        password=str(input("password:"))
    l.append(password)
    r=random.randint(1,100)
    if r not in m:
        m.append(r)
        d[r]=l
    f.write(str(d))
    f.close()
    print("do you want to continue:")
    print("""menu:
        1.register
        2.log in
        3.exit""")
    choice=int(input("enter choice:"))
    return choice
def login():
    print("******************login page*******************")
    print("enter user id:")
    user_id=int(input())
    password1=str(input())
    l=[]
    f=open("bank.txt","r")
    r=eval(f.read())
    if(password1 in r[user_id]):
        print("successful log in")
        r={"amount":2000,"withdraw":0,"history":[]}
        d[user_id].append(r)
        account_details(user_id)
    f.close()
    print("do you want to continue:")
    print("""menu:
        1.register
        2.log in
        3.exit""")
    choice=int(input("enter choice:"))
    return choice
def account_details(user_id):
    print("******************account details*******************")
    print("""choice:
        1.amount_balance
        2.withdraw
        3.deposit
        4.history
        5.return back to login page
    """)
    z=int(input("enter choice:"))
    while(z>=1 and z<=5):
        if(z==1):
            print(d[user_id][4]["amount"])
            z=int(input("enter choice:"))
        elif(z==2):
            amount=int(input("amount want to be withdraw"))
            amount_available=d[user_id][4]["amount"]
            if(amount_available<amount):
                print("low balance")
                z=int(input("enter choice:"))
            else:
                print("amount withdraw %d"%(amount))
                print("amount available in your account %d"%(amount_available-amount))
                d[user_id][4]["amount"]=amount_available-amount
                d[user_id][4]["history"].append("-"+str(amount))
                z=int(input("enter choice:"))
        elif(z==3):
            amount=int(input("amount want to be deposited"))
            d[user_id][4]["amount"]=amount+d[user_id][4]["amount"]
            d[user_id][4]["history"].append("+"+str(amount))
            z=int(input("enter choice:"))
        elif(z==4):
            h=d[user_id][4]["history"]
            print("transaction history")
            print(h)
            z=int(input("enter choice:"))
        elif(z==5):
            f=open("aa.txt","w")
            f.write(str(d))
            f.close()
            break
    
while(choice>=1 and choice<=3):
    if(choice==1):
        choice=register()
    if(choice==2):
        choice=login()
    if(choice==3):
        print("Thank for using our bank :)")
        break

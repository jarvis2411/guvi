import random
print("Welcome to JK Bank\n")
d={}
def read():
    f=open("banker.txt","r")
    
print("""menu:
        1.register
        2.log in""")
choice=int(input("enter choice"))
def register():
    f=open("bank.txt","w")
    l=[]
    print("register")
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
    print(r)
    d[r]=l
    f.write(str(d))
    f.close()
    print("do you want to continue:")
    choice=int(input("press 2 to login"))
    return choice
def login():
    print("enter user id:")
    user_id=int(input())
    password1=str(input())
    l=[]
    f=open("bank.txt","r")
    r=eval(f.read())
    if(password1 in r[user_id]):
        print("successful log in")
    f.close()
    print("do you want to continue:")
    choice=int(input("press 2 to login"))
    return choice
while(choice>=1 and choice<=2):
    if(choice==1):
        choice=register()
    if(choice==2):
        choice=login()

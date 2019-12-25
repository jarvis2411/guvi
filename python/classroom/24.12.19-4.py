i = 3
while(i):
    a = input("Enter the username:")
    if a == "admin":
        i = 3
        while(i):
            b = input("Enter the password:")
            if b == "password":
                print("Login successful")
                a = int(input("Enter the source in kilometers:"))
                b = int(input("Enter the destination in kilometers:"))
                print("The distance of the travel is",b-a,"kms")
                i =0
                break
            else:
                print("Password incorrect")
                i = i -1
    else:
        print("Username not valid")
        i = i -1

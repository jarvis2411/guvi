i = 3
while(i):
    a = input("Enter the username:")
    if a == "admin":
        i = 3
        while(i):
            b = input("Enter the password:")
            if b == "password":
                print("Login successful")
                i = 0
                break
            else:
                print("Password incorrect")
                i = i -1
    else:
        print("Username not valid")
        i = i -1

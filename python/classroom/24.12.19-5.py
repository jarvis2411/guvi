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
                print("1.Micro 2.Luxury 3.Sedan 4.SUV")
                c = input("Select your car type :")
                if c == "micro":
                    print("1.Hyundai Eon 2.Tata Indica 3.Maruthi 800")
                    d = input("Select your car model")
                    print("You have booked",d,"for",b-a,"kms")
                elif c == "luxury":
                    print("1.Benz 2.BMW 3.Audi")
                    d = input("Select your car model")
                    print("You have booked",d,"for",b-a,"kms")
                elif c == "SUV":
                    print("1.Ecosport 2.Duster 3.Scorpio")
                    d = input("Select your car model")
                    print("You have booked",d,"for",b-a,"kms")
                else: 
                    print("1.City 2.Dzire 3.Verna")
                    d = input("Select your car model")
                    print("You have booked",d,"for",b-a,"kms")
                i =0
                break
            else:
                print("Password incorrect")
                i = i -1
    else:
        print("Username not valid")
        i = i -1

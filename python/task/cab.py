t = 0
i = 3
cost = 0
while(i):
    name = input("Enter the username:")
    if name == "jerry":
        i = 3
        while(i):
            password = input("Enter the password:")
            if password == "praghadesh":
                print("Login successful")
                a = input("Enter the source:")
                b = int(input("Enter the destination in kilometers:"))
                r = 3
                while(r):
                    print("1.Micro 2.Luxury 3.Sedan 4.SUV")
                    c = input("Select your car type :")
                    if str.upper(c) == "MICRO":                      
                        d = input("Select your car model:")
                        p = 3
                        while(p):
                            print("1.Hyundai Eon 2.Tata Indica 3.Maruthi 800")
                            d = input("Select your car model:")
                            if str.upper(d) == "HYUNDAI EON" or str.upper(d) == "TATA INDICA" or str.upper(d) =="MARUTHI 800":
                                p = 0
                                t = 1
                            else:
                                print("Incorrect car model!!! Please select the correct car model")
                                p -= 1
                        if b> 20:
                            cost = b*14
                        else:
                             cost = b*6                  
                        r = 0
                    elif str.upper(c) == "LUXURY":
                        p = 3
                        while(p):
                            print("1.Benz 2.BMW 3.Audi")
                            d = input("Select your car model:")
                            if str.upper(d) == "BENZ" or str.upper(d) == "BMW" or str.upper(d) =="AUDI":
                                p = 0
                                t = 1
                            else:
                                print("Incorrect car model!!! Please select the correct car model")
                                p -= 1
                        if b> 20:
                            cost = b*30
                        else:
                             cost = b*25
                        r = 0
                    elif str.upper(c) == "SUV":
                        p = 3
                        while(p):
                            print("1.Ecosport 2.Duster 3.Scorpio")
                            d = input("Select your car model:")
                            if str.upper(d) == "ECOSPORT" or str.upper(d) == "DUSTER" or str.upper(d) =="SCORPIO":
                                p = 0
                                t = 1
                            else:
                                print("Incorrect car model!!! Please select the correct car model")
                                p -= 1
                        if b> 20:
                            cost = b*19
                        else:
                             cost = b*11
                        r = 0
                    elif str.upper(c) == "SEDAN":
                        p = 3
                        while(p):
                            print("1.City 2.Dzire 3.Verna")
                            d = input("Select your car model:")
                            if  str.upper(d) == "CITY" or str.upper(d) == "DZIRE" or str.upper(d) =="VERNA":
                                p = 0
                                t = 1
                            else:
                                print("Incorrect car model!!! Please select the correct car model")
                                p -= 1                                
                        if b> 20:
                            cost = b*16
                        else:
                             cost = b*8
                        r = 0
                    else:
                        r -= 1
                        if r != 0:
                            print("Incorrect car type!!! Please select the correct car model")    
                i =0
                break
            else:
                i -= 1
                if i != 0:
                    print("Password incorrect")
    else:
        i -= 1
        if i !=  0:
            print("Username not valid")
if t == 1:        
    print("Name:",str.upper(name))
    print("Source:",str.upper(a))
    print("Disatance:",b)
    print("Car type:",str.upper(c))
    print("Car model:",str.upper(d))
    print("Total fare:",cost)
else:
    print("Better Luck Next Time!!!!!")

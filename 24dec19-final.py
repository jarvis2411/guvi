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
                    if c == "micro":                      
                        d = input("Select your car model:")
                        p = 3
                        while(p):
                            print("1.Hyundai Eon 2.Tata Indica 3.Maruthi 800")
                            d = input("Select your car model:")
                            if d == "hyundai eon" or d == "tata indica" or d =="maruthi 800":
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
                    elif c == "luxury":
                        p = 3
                        while(p):
                            print("1.Benz 2.BMW 3.Audi")
                            d = input("Select your car model:")
                            if d == "benz" or d == "bmw" or d =="audi":
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
                    elif c == "suv":
                        p = 3
                        while(p):
                            print("1.Ecosport 2.Duster 3.Scorpio")
                            d = input("Select your car model:")
                            if d == "ecosport" or d == "duster" or d =="scorpio":
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
                    elif c == "sedan":
                        p = 3
                        while(p):
                            print("1.City 2.Dzire 3.Verna")
                            d = input("Select your car model:")
                            if d == "city" or d == "dzire" or d =="verna":
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
    print("Name:",name)
    print("Source:",a)
    print("Disatance:",b)
    print("Car type:",c)
    print("Car model:",d)
    print("Total fare:",cost)
else:
    print("Better Luck Next Time!!!!!")

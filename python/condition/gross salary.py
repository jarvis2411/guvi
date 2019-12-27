a = int(input("Enter your basic salary:"))
if a > 20000:
    print("Your gross salary is Rs",a+(a*0.30*0.95))
elif a <= 20000:
    print("Your gross salary is Rs",a+(a*0.25*0.90))
else:
    print("Your gross salary is Rs",a+(a*0.20*0.80))

a = int(input("Enter the electricity unit charges:"))
b,c = 0,0
if a <= 50:
    b = a*0.5
elif a <= 150:
    b = a*0.75
elif a <= 250:
    b = a*1.2
else:
    b = a*1.5

print("The total electricity bill is Rs.",b+(b*0.20))

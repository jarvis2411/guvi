a = int(input("Physics Mark:"))
b = int(input("Chemistry Mark:"))
c = int(input("Mathematics Mark:"))
d = int(input("Biology Mark:"))
e = int(input("Computer Science Mark:"))
f = (a+b+c+d+e)//5
if f >= 90:
    print("Your percentage is",f,"% and your grade is A")
elif f >= 80:
    print("Your percentage is",f,"% and your grade is B")
elif f >= 70:
    print("Your percentage is",f,"% and your grade is C")
elif f >= 60:
    print("Your percentage is",f,"% and your grade is D")
elif f >= 40:
    print("Your percentage is",f,"% and your grade is E")
else:
    print("Your percentage is",f,"% and your grade is F")

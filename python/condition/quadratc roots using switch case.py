print("a(x**2) + b(x) + c = 0")
print("Enter the values of a,b,c")
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
d = b**2 - 4*(a*c)
if d > 0:
    x = (-b - (d**0.5))/(2*a)
    y = (-b + (d**0.5))/(2*a)
    print(" Roots are real and different")
    print("The roots are",x,"and",y)
elif d == 0:
    x = (-b - (d**0.5))/(2*a)
    y = (-b + (d**0.5))/(2*a)
    print(" Roots are real and same")
    print("The roots are",x,"and",y)
else:
    print("Roots are complex")
    print(-b/(2*a),"+i",d**0.5)
    print(-b/(2*a),"-i",d**0.5)
    

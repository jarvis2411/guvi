a = int(input("Enter the input1:"))
c = input("Enter the operation:")
b = int(input("Enter the input2:"))
if c == '+':
    print(a,"+",b,"=",a+b)
elif c == '-':
    print(a,"-",b,"=",a-b)
elif c == '*':
    print(a,"*",b,"=",a*b)
elif c == '/':
    print(a,"/",b,"=",a/b)
elif c == '%':
    print(a,"%",b,"=",a%b)
else:
    print("Invalid option")

def join(s,b):
    a = len(s)
    for i in range(0,a):
        print(s[i],end = b)
s = input("Enter the string:")
b = input("Enter the character to be added:")
print("The string after joined is:",end = " ")
join(s,b)

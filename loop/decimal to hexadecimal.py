d = int(input("Enter the decimal number:"))
m = d
r,t = 0,[]
while(d>0):
    r = d % 16
    if(r<10):
        t.append(chr(r+48))
    else:
        t.append(chr(r+55))
    d = d//16
t = t[::-1]
print("The hexadecimal of decimal number",m,"is", end = " ")
for i in range(0,len(t)):
    print(t[i],end='')

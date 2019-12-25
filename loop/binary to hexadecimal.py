n = int(input("Enter the binary number:"))
m = n
d = 0
r,t = 0,0
while(n>0):
    r = n %10
    d = d + (r*(2**t))
    t = t + 1
    n = n//10
r,t = 0,[]
while(d>0):
    r = d % 16
    if(r<10):
        t.append(chr(r+48))
    else:
        t.append(chr(r+55))
    d = d//16
t = t[::-1]
print("The hexadecimal of binary number",m,"is",end = " ")
for i in range(0,len(t)):
    print(t[i],end='')

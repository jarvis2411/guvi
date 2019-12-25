n = input("Enter the octal number:")
a = len(n)
d = 0
j = 0
for i in range(a-1,-1,-1):
    d += (int(n[i]) *(8**j))
    j += 1
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
print("The hexadecimal of octal number",n,"is", end = " ")
for i in range(0,len(t)):
    print(t[i],end='')


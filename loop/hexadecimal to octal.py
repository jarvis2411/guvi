n = input("Enter the hexadecimal number:")
a = len(n)
c,d = 0,0
j = 0
for i in range(a-1,-1,-1):
    if  ord(n[i]) - 48 < 10 :
        d = int(n[i])
    elif ord(n[i]) > 64 and ord(n[i]) < 71:
        d = (ord(n[i])) - 55
    else:
        print("Type error")
        c = 0
        break
    c += d * (16 ** j)
    j += 1
if c > 0:
    m = c
    r,t = 0,[]
    while(c>0):
        r = c % 8
        t.append(chr(r+48))
        c = c//8
    t = t[::-1]
    print("The octal of the hexadecimal number",n,"is",end = " ")
    for i in range(0,len(t)):
        print(t[i],end='')

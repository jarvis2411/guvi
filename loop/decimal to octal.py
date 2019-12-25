d = int(input("Enter the decimal number:"))
m = d
r,t = 0,[]
while(d>0):
    r = d % 8
    t.append(chr(r+48))
    d = d//8
t = t[::-1]
print("The octal of the decimal number",m,"is",end = " ")
for i in range(0,len(t)):
    print(t[i],end='')

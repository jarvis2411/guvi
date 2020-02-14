'''Given a binary number convert it into octal format.
Sample Testcase :
INPUT
1100100
OUTPUT
144'''
n = int(input())
d = 0
r,t = 0,0
#h = 0
while(n>0):
    r = n %10
    d = d + (r*(2**t))
    t = t + 1
    n = n//10
r,t = 0,[]
while(d>0):
    r = d % 8
    t.append(chr(r+48))
    d = d//8
t = t[::-1]
for i in range(0,len(t)):
    print(t[i],end='')
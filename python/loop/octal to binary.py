n = int(input("Enter the octal number:"))
m = n
o = 0
b = ['000','001','010','011','100','101','110','111']
d = []
while n>0:
    o = n % 10
    d.append(b[o])
    n = n // 10
print("The binary number of octal number",m,"is",end = " ")
for i in range(len(d)-1,-1,-1):
    print(d[i],end = "")

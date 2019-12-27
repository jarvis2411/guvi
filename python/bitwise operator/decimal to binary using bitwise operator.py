n = int(input("Enter the decimal number:"))
m = 7
o = n
p = [ ]
while  m>= 0:
    p.append(1 if n &1 else 0)
    m -= 1
    n >>= 1
print("The number",o,"is converted as",end = " ")
print(p[7],end="")
print(p[6],end="")
print(p[5],end="")
print(p[4],end="")
print(p[3],end="")
print(p[2],end="")
print(p[1],end="")
print(p[0],end="")


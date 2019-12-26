def add(a):
    b = int(input())
    print(a+b)
def sub(a):
    b = int(input())
    print(a-b)
def mul(a):
    b = int(input())
    print(a*b)
def div(a):
    b = int(input())
    print(a/b)
a = int(input())
c = input()
if c == '+':
    add(a)
elif c == '-':
    sub(a)
elif c == '*':
    mul(a)
elif c == '/':
    div(a)
else:
    print("Invalid option")

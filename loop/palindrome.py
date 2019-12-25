n = int(input("Enter the number:"))
m = n
c = 0
while n> 0:
    c = c*10 + n%10
    n = n//10    
if c == m:
    print("The number",m,"is a palindrome")
else:
    print("The number",m,"is not a palindrome")

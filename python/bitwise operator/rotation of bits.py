n = int(input("Enter the number to be rotated:"))
a = int(input("Enter the bits to be rotated:"))
print("1.Left Rotation 2.Right Rotation")
b = int(input("Enter your choice:"))
if b == 1:
    print("The number",n,"after left rotation by",a,"bits is", n << a)
elif b == 2:
    print("The number",n,"after right rotation by",a,"bits is", n >> a)
else:
    print("Invalid choice")

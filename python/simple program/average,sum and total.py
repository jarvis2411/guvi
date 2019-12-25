a = int(input("Enter the number of the subjects:"))
b = 0
for i in range(1,a +1):
    c = int(input("Enter the mark of the subject:"))
    b = b + c
print("The total marks is",b)
print("The average marks is",b/a)
print("The percentage of the marks is",b/a)

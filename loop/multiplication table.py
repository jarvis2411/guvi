b = int(input("Enter the table to be performed: "))
m = int(input("Enter the range upto which multiplication has to be performed: "))
print("The multiplication table of ",b,":")
for i in range(1,m+1):
    print(b,"*",i,"=",b*i)

def reverse(s):
    a = len(s)
    for i in range(a-1,-1,-1):
        print(s[i],end = "")

s = input("Enter the string to be reversed:")
print("The reversed string is:",end = " ")
reverse(s)

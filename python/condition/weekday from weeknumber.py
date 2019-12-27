n = int(input("Enter the week number:"))
a = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
if n>=1 and n <= 7:
    print(a[n-1])
else:
    print("Invalid week number")

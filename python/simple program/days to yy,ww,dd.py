n = int(input("Enter the number of days :"))
a = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
print((n//365),"years",(n//7)%52,"weeks",(a[n%7]))

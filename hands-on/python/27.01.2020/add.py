a = int(input())
b = int(input())
c = a + b
d = open("add.txt","w+")
d.write("The addition of %d and %d is %d\r\n"%(a,b,c))
d.close()

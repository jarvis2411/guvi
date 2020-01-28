a = open ("1.txt","w+")
for i in range(0,3):
  a.write("%d th line \r\n"%(i+1))
a.close()

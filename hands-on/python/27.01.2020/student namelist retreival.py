f =  open("7.txt","r")
'''size = int(input("Enter the class strength:"))
for i in range(1,size+1):
  print("Enter the mark of",i,"student",end = ":")
  a = int(input())
  d[i] = a
f.write("%s"%(d))'''
c = eval(f.read())
print(c)
print(c[3][0])
f.close()

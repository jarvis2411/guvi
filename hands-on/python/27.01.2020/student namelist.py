f =  open("student.txt","a+")
f.seek(0)
g = f.read()
print("lll",g,len(g))
if len(g) == 0 :
  d = { }    
  size = int(input("Enter the class strength:"))
  for i in range(1,size+1):
    id = int(input("Enter the id:"))
    print("Enter the mark of",id,"student",end = ":")
    a = int(input())
    d[id] = a
else:
  #f =  open("student.txt","a+")
  id = int(input("Enter the id:"))
  print("Enter the mark of",id,"student",end = ":")
  a = int(input())
  f.seek(0)
  d = eval(f.read())
  d.update({id:a})
  print(d)
  f.close()
f = open("student.txt","w+")
f.seek(0)
f.write("%s"%(d))
f.close()

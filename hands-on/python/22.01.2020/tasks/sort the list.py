l = [3, 1, 4, 2, 5]
k = []
while len(l) > 0:
  for i in l:
    mini = i
    #print(mini) 
    for j in range(0,len(l)):
      if mini > l[j]:
        mini = l[j]
      else:
        mini = mini
    k.append(mini)
    l.remove(mini)
    #print(k,l)
print(k)

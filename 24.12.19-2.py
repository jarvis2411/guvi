a =[3,7,6,2,1]
i=0
while i<len(a):
    if(a[i] == 6):
        i += 1
        continue
    else:
        print(a[i])
        i = i+1    

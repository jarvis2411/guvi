import os
d={'mira': 9836725618,
 'arvind': 6579839028,
 'tintoo':4748959027,
 'Isco':3984762973}
#d=dict()
val=""
print("***CONTACT MANAGER***")
if os.path.getsize('C:/Users/Lavanyaa/Desktop/Guvi/dict.txt') == 0 :
    print("Contact Book is empty")
    f = open('C:/Users/Lavanyaa/Desktop/Guvi/dict.txt', 'a')
    f.write( str(d) )
    f.close()
while(val != 'Q'):
    print("Press '1' Get contact\n Press '2' Add Contact\n Press '3' Update contact \n Press 'Q' To Exit")
    val=input("Enter your option:")
    if(val == '1'):
        n=input("Enter the person name :")
        f = open('C:/Users/Lavanyaa/Desktop/Guvi/dict.txt', 'r')
        f.seek(0)
        g_no=eval(f.read())
        if n in g_no:
            print(g_no.get(n))
        else:
            print("contact not found")
        f.close()
    elif(val == '2'):
        k=input("name:")
        v=int(input('contact no:'))
        f=open('C:/Users/Lavanyaa/Desktop/Guvi/dict.txt', 'r+')
        g_no=eval(f.read())
        if k in g_no:
            print("Name already exist")
            break;
        else:
            f=open('C:/Users/Lavanyaa/Desktop/Guvi/dict.txt', 'w')
            g_no.update({k:v})
            #f.seek(0)
            #f.truncate()
            f.write(str(g_no))   
            f.close()
    elif(val == '3'):
        n=input("Enter the person name :")
        f = open('C:/Users/Lavanyaa/Desktop/Guvi/dict.txt', 'r+')
        f.seek(0)
        g_no=eval(f.read())
        if n in g_no:
            v=int(input("Enter the new contact number:"))
            g_no[n]=v
            f.seek(0)
            f.truncate()
            f.write(str(g_no))
        else:
            print("Contact not found")       
        f.close()
    elif(val == 'Q'):
        exit()
    


# f = open("C:/Users/Lavanyaa/Desktop/Guvi/dict.txt","w")
# f.write( str(d) )
# f.close()

def add(a,b):
    return a+b
l = [(1,2),(2,3),(4,5)]
m = []
for i in l:
    m.append(add(*i))
print(m)

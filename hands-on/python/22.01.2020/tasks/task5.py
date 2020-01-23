wtf = {2: [1, 2, 3], 'a': {'b': {'c': {'d': {'e': [1, 2, 3]}}}}}

#Get the first array value for the key 2
print(wtf[2])
#Print all the array value for the key 2
a = wtf[2]
for i in a:
  print(i,end = " ")
#Print value of key 'a','b','c','d','e'
print(wtf['a'])
print(wtf['a']['b'])
print(wtf['a']['b']['c'])
print(wtf['a']['b']['c']['d'])
print(wtf['a']['b']['c']['d']['e'])
#Print the sum of the array with key 'e'
b = wtf['a']['b']['c']['d']['e']
c = 0
for i in b:
  c += i
print(c)
#set value of key 'e' to ['Chera','Chola','Pandiya']
wtf['a']['b']['c']['d']['e'] = ['Chera','Chola','Pandiya']
print(wtf['a']['b']['c']['d']['e'])

#Print my Bill

prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {'apple': 1,    'banana': 6}
a,c = 0,0
for x in my_purchase:
  for y in prices:
    if x == y:
      a = my_purchase[x]*prices[x]
      print("The price of",my_purchase[x],x,"is",a)
      c = c + a
print("The total bill amount is",c)

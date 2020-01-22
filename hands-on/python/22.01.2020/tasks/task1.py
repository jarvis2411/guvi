l = [
    {
        "color": "red",
        "value": "#f00"
    },
    {
        "color": "green",
        "value": "#0f0"
    },
    {
        "color": "blue",
        "value": "#00f"
    }
]
print("The hex values in the list:",end = " ")
for x in l:
  print(x["value"],end = " ")
print()
print("Hex value of green:",end = " ")
for x in l:
  if x['color'] == 'green':
    print(x['value'])
print()
print("The values in the list:")
for x in l:
  for y in x.items():
    for z in y:
      print(z,end = " ")
    print()
    

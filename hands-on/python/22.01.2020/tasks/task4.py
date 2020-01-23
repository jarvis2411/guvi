#print the items
#print the roles

junk = {
    "characters": {
        "Lonestar": {
            "id": 55923,
            "role": "renegade",
            "items": [
                "space winnebago",
                "leather jacket"
            ]
        },
        "Barfolomew": {
            "id": 55924,
            "role": "mawg",
            "items": [
                "peanut butter jar",
                "waggy tail"
            ]
        },
        "Dark Helmet": {
            "id": 99999,
            "role": "Good is dumb",
            "items": [
                "Shwartz",
                "helmet"
            ]
        },
        "Skroob": {
            "id": 12345,
            "role": "Spaceballs CEO",
            "items": [
                "luggage"
            ]
        }
    }
}
for x in junk:
  #print(x)
  for y in junk[x]:
    #print(y)
    for z in junk[x][y]:
      #print(z)
      #for w in junk[x][y][z]:
      if z == 'items' or z == 'role':
        print(z,"of",y,"is",junk[x][y][z])

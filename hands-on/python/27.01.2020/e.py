def login(id,password):
  g = eval(f.read())
  if id in g.items():
    if password == g[id][-1]:
      print("Login successfull")
    else:
      print("Invalid password")
  else:
    print("Invalid user id..... If you are new kindly signup... or check with different user credentials")

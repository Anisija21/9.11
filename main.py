a = int(input("Ievadiet skolēna vidējo atzīmi: "))
b = int(input("Ievadiet skolēna vidējo atzīmi: "))
c = int(input("Ievadiet skolēna vidējo atzīmi: "))

if a > 9:
  print("Skolēns 1 ir teicamnieks")
else:
  print("Skolēns 1 nav teicamnieks")
  if b > 9:
    print("Skolēns 2 ir teicamnieks")
  else:
    print("Skolēns 2 nav teicamnieks")
    if c > 9:
      print("Skolēns 3 ir teicamnieks")
    else:
      print("Skolēns 3 nav teicamnieks")
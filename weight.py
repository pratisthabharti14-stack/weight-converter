weight = int(input("Weight: "))
unit = input( "(K)g or (L)bs:  ")

if unit.upper() == "K":
      converted = weight * 2.20462
      print( "weight in Lbs: " + str(converted))

else:
      converted = weight / 2.20462
      print("weight in Kgs: " + str( converted)) 
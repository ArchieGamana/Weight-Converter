
weight = int(input("Enter your weight: "))
unit = input("Choose (K)kg or (L)lbs: ")
if unit.upper() == 'K':
    converted = (weight / 0.45)
    print("Weight in Lbs: " + str(converted))
else:
    converted =(weight * 0.45)
    print("Weight in Lbs: " + str(converted))


weight = input("Weight: ")

weight_unit = input("(K)gs or (L)bs: ").lower()

if weight_unit == "k":
    ret = float(weight) * 2.20462262

    print("Weight in Lbs:", int(ret))
else:
    ret = float(weight) * 0.45359237
    print("Weight in Kg:", round(ret, 1))

print("DONE")

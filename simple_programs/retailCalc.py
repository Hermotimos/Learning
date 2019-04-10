# retailCalc enables user to recalculate given ratio to more understandable units via proportion
# ex. 700g of sth costs 24.99$ - how much is it for 1000g?

ratio1_value1 = float(input("Known ratio's 1st attribute: "))
ratio1_value2 = float(input("Known ratio's 2nd attribute: "))

ratio2_value1 = float(input("Searched ratio's 1st attribute (if unknown type '0' or 'n'): "))
ratio2_value2 = float(input("Searched ratio's 2nd attribute (if unknown type '0' or 'n'): "))

if not (ratio2_value1 == 0 and ratio2_value2 == 0):
    if ratio2_value1 == 0:
        ratio2_value1 = ratio1_value1/ratio1_value2 * ratio2_value2
        ratio2_value1 = round(ratio2_value1, 2)
    elif ratio2_value2 == 0:
        ratio2_value2 = ratio2_value1 * ratio1_value2 / ratio1_value1
        ratio2_value2 = round(ratio2_value2, 2)
    print(ratio1_value1, "/", ratio1_value2, "=", ratio2_value1, "/", ratio2_value2)
else:
    print("Wrong data entered! Ratio 0/0 cannot be resolved!")


# maybe: import time => time.sleep(10) for use outside IDE
# OR better: infinite while loop asking for new task
#  [to do] exception: user types str instead of number
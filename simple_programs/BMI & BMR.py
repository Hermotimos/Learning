"""
    Calculates personal BMR (basal metabolic rate) and resulting daily caloric needs based on user input.
    This simple program was written for learning and exercise purposes.

    Sources:
        https://www.flynerd.pl/2016/06/jak-obliczyc-zapotrzebowanie-kaloryczne-krok-po-kroku.html
"""


# Calculating basal metabolic rate (BMR)
sex_mod = 0
sex = input("Enter 'M' for male or 'F' for female\n")

if sex == "M":
    sex_mod = 5
elif sex == 'F':
    sex_mod = -161
else:
    print("Wrong value entered")

weight = float(input("Enter your weight in kilograms\n"))
height = float(input("Enter your height in centimeters\n"))
age = float(input("Enter your age\n"))

bmr = 10*weight + 6.25*height - 5*age + sex_mod

# Calculating lifestyle modificator:
life_style = int(input("What is your lifestyle?\n"
                   "1 - Sedentary work / no physical activity\n"
                   "2 - Nonphysical work / little physical activity\n"
                   "3 - Light physical work / regular exercise 3-4x/week\n"
                   "4 - Physical work / regular exercise min. 5x/week\n"
                   "5 - Hard physical work / regular exercise 7x/week\n"))
life_style_mod = 0
if life_style == 1:
    life_style_mod = 1.2
elif life_style == 2:
    life_style_mod = 1.4
elif life_style == 3:
    life_style_mod = 1.6
elif life_style == 4:
    life_style_mod = 1.8
elif life_style == 5:
    life_style_mod = 2.0
else:
    print("Wrong value entered")

print("\nRESULT:\nYour basal metabolic rate (BMR) = 'no activity' mode : ", bmr, "kcal")
print("Caloric needs for your lifestyle: ", bmr * life_style_mod, "kcal")



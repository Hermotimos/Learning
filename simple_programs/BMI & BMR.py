"""
    Calculates personal BMR (basal metabolic rate) and resulting daily caloric needs based on user input.
    This simple program was written for learning and exercise purposes.

    Sources:
        https://www.flynerd.pl/2016/06/jak-obliczyc-zapotrzebowanie-kaloryczne-krok-po-kroku.html
"""


def calculate_bmr():

    def ask_sex(): return input("Enter 'M' for male or 'F' for female\n")
    def ask_weight(): return float(input("Enter your weight in kilograms\n"))
    def ask_height(): return float(input("Enter your height in centimeters\n"))
    def ask_age(): return float(input("Enter your age\n"))

    def calculate_sex_mod(genetic_sex):
        mod = 0
        if genetic_sex == "M":
            mod = 5
        elif genetic_sex == 'F':
            mod = -161
        return mod

    sex = ask_sex()
    weight = ask_weight()
    height = ask_height()
    age = ask_age()
    sex_mod = calculate_sex_mod(sex)

    bmr = 10 * weight + 6.25 * height - 5 * age + sex_mod
    return bmr


def calculate_lifestyle_mod():
    def ask_lifestyle():
        life_style_id = int(input("What is your lifestyle?\n"
                                  "1 - Sedentary work / no physical activity\n"
                                  "2 - Nonphysical work / little physical activity\n"
                                  "3 - Light physical work / regular exercise 3-4x/week\n"
                                  "4 - Physical work / regular exercise min. 5x/week\n"
                                  "5 - Hard physical work / regular exercise 7x/week\n"))
        return life_style_id

    lifestyle_id = ask_lifestyle()
    life_style_mod = 1
    if lifestyle_id == 1:
        life_style_mod = 1.2
    elif lifestyle_id == 2:
        life_style_mod = 1.4
    elif lifestyle_id == 3:
        life_style_mod = 1.6
    elif lifestyle_id == 4:
        life_style_mod = 1.8
    elif lifestyle_id == 5:
        life_style_mod = 2.0
    return life_style_mod


def calculate_caloric_needs(bmr):
    mod = calculate_lifestyle_mod()
    caloric_needs = bmr * mod
    return caloric_needs


def main():
    bmr = calculate_bmr()
    caloric_needs = calculate_caloric_needs(bmr)
    print("\nRESULT:\nYour basal metabolic rate (BMR) = 'no activity' mode : ", bmr, "kcal")
    print("Caloric needs for your lifestyle: ", caloric_needs, "kcal")

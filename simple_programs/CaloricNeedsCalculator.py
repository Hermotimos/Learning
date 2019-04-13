"""
    Calculates personal BMR (basal metabolic rate) and resulting daily caloric needs based on user input.
    This simple program was written for learning and exercise purposes.

    Used features:
        - user defined funtions
        - nested functions
        - decorators
        - if else statements
        - assertions, exception handling

    Sources:
        https://www.flynerd.pl/2016/06/jak-obliczyc-zapotrzebowanie-kaloryczne-krok-po-kroku.html
"""


def main():
    """ Print info about BMR and caloric needs based on user's input. """
    bmr = round(calculate_bmr(), 2)
    caloric_needs = round(calculate_caloric_needs(bmr), 2)
    print(f"\nRESULT:\nYour basal metabolic rate (BMR), i.e. 'no activity' mode : {bmr} kcal daily.")
    print(f"Caloric needs for your lifestyle: {caloric_needs} kcal daily.")


def calculate_caloric_needs(bmr):
    """ Apply life style modifier to BMR to calculate and return caloric needs. """
    mod = calculate_lifestyle_mod()
    caloric_needs = bmr * mod
    return caloric_needs


def calculate_lifestyle_mod():
    """ Calculate and return life style modifier to be applied to BMR. """

    @verify_answer_decorator
    def ask_lifestyle():
        """ Ask user's life style and return it's code. """
        answ = input("What is your lifestyle?\n"
                     "1 - Sedentary work / no physical activity\n"
                     "2 - Nonphysical work / little physical activity\n"
                     "3 - Light physical work / regular exercise 3-4x/week\n"
                     "4 - Physical work / regular exercise min. 5x/week\n"
                     "5 - Hard physical work / regular exercise 7x/week\n")
        return answ

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


def calculate_bmr():
    """ Ask user's sex, weight, height, age to calculate and return BMR. """

    @verify_answer_decorator
    def ask_sex(): return input("Enter 'm' for male or 'f' for female\n").lower()
    @verify_answer_decorator
    def ask_weight(): return input("Enter your weight in kilograms\n")
    @verify_answer_decorator
    def ask_height(): return input("Enter your height in centimeters\n")
    @verify_answer_decorator
    def ask_age(): return input("Enter your age\n")

    def calculate_sex_mod(biological_sex):
        """ Calculate and return sex modifier based on user's stated biological sex. """
        mod = 0
        if biological_sex == "M":
            mod = 5
        elif biological_sex == 'F':
            mod = -161
        return mod

    sex = ask_sex()
    weight = ask_weight()
    height = ask_height()
    age = ask_age()
    sex_mod = calculate_sex_mod(sex)

    bmr = 10 * weight + 6.25 * height - 5 * age + sex_mod
    return bmr


def verify_answer_decorator(func):
    """ Verify assertions about user input. If false give error message and call input-functions recursively. """

    def wrapper():
        try:
            value = func()
            if func.__name__ == 'ask_lifestyle':
                assert 0 < int(value) < 6
                return int(value)
            if func.__name__ == 'ask_sex':
                assert value in ('m', 'f')
                return value
            if func.__name__ == 'ask_weight' or 'ask_height' or 'ask_age':
                assert float(value)
                return float(value)
        except (AssertionError, ValueError):
            print('Wong value entered. Please try again.')
            return wrapper()

    return wrapper


main()

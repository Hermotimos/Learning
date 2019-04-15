"""
    This simple program was written for learning and exercise purposes.
    Calculates the amount of money in time deposit after given time with monthly compound interest payout.

    Features involved:
        - nested for loop
        - f-strings
        - docstring

    Sources:
        https://www.flynerd.pl/2017/01/python-3-formatowanie-napisow.html
"""


depositStart = float(input("How much money would you like to put into time deposit? \n"))
yearlyInterestRate = float(input("What is the annual interest rate in %? \n")) / 100
depositDuration = int(input("For how many years should the deposit last? \n"))

depositResult = depositStart
for year in range(depositDuration):
    for month in range(0, 12):
        depositResult += depositResult * (yearlyInterestRate/12)

print(f"After {depositDuration} year(s) your time deposit of {depositStart} at {yearlyInterestRate} interest rate "
      f"will amount to {depositResult}")


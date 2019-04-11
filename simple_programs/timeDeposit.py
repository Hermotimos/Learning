# enables user to predict the amount of money in time deposit after given time
# interest rate is added monthly

depositStart = float(input("How much money would you like to put into time deposit? "))
yearlyInterestRate = float(input("What is the annual interest rate in %? ")) / 100
depositDuration = int(input("For how many years should the deposit last? "))

depositResult = depositStart
for year in range(depositDuration):
    for month in range(0, 12):
        depositResult += depositResult * (yearlyInterestRate/12)

print(f"After {depositDuration} year(s) your time deposit of {depositStart} at {yearlyInterestRate} interest rate "
      f"will give {depositResult}")

# [to do] exceptions: floats instead of integers - months possible to choose
# [to do] other exceptions?

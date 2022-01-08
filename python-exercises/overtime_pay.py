hoursInput = (input("Please enter number of hours worked: "))
rateInput = (input("Please enter your hourly rate: "))
try:
    hours = float(hoursInput)
    rate = float(rateInput)
except:
    print("Please enter a numeric input.")

print(hours, rate)
if hours > 40:
    #print("Overtime")
    regular = (hours * rate)
    overtime = (hours - 40.0) * (rate * 0.5)
    totalpay = regular + overtime
    print("Your total pay including overtime is: ", totalpay)
else:
    regular = (hours * rate)
    print("Your total pay is: ", regular)
#Project: Tip calculator
print("Welcome to the tip calculator")
bill=float(input("How much is the bill?\n"))
tip=int(input("What percentage you want to give tip? (10% or 12% or 15%)\n"))
split=int(input("In how many people to split the bill?\n"))
total_bill=bill+(bill*tip/100)
perhead=round(total_bill/split,2)
print(f"Each person should pay {perhead}")

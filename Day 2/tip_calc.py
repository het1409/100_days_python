print("Welcome to the tip calcualtor.")
total_bill = float(input("What was the total bill? £"))
percentage = int(input("What percentage tip would yoou like to give? 10, 12, or 15?"))
bill_split = int(input("How many people to splt the bill?"))

#calculation
tip = total_bill * (percentage / 100)
new_bill = total_bill + tip
final_split = new_bill / bill_split

print(f"Each person should pay: £{final_split}")


#EXPLANATION
#if total bill is 100 and if tip is 12% then multiply total bill with tip and add it to the total bill
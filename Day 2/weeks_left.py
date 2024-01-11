#Assuming a person lives for 90 years, calculate how many weeks they have left to live based on their current age.

age = int(input())

years = 90 - age
weeks_left = years * 52
print(f"you have {weeks_left} weeks left")
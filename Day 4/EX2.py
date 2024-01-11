import random

names = input("enter names seperated by ',': ")
lst = names.split(", ")

names_items = len(lst)
print(lst)

r_names = random.randint(0, names_items - 1)
bill = lst[r_names]

print(bill + " will pay the bill")
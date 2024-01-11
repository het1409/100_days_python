print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

comb_names = name1 + name2
new_names = comb_names.lower()

t = new_names.count("t")
r = new_names.count("r")
u = new_names.count("u")
e = new_names.count("e")

count = t + r + u + e
a = str(count)

l = new_names.count("l")
o = new_names.count("o")
v = new_names.count("v")
e = new_names.count("e")

l_count = l + o + v + e
b = str(l_count)

new_count = a + b
fc = int(new_count)
#print(new_count)

if fc < 10 or fc > 90:
  print(f"Your score is {fc}, you go together like coke and mentos.")
elif fc >= 40 and fc <= 50:
  print(f"Your score is {fc}, you are alright together.")
else:
  print(f"Your score is {fc}.")
import random
moves = ["rock", "paper", "scissor"]
rock = """  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

print(rock)

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
print(paper)

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print(scissor)


p1 = input()
p2 = random.choice(moves)

print(f"p2 chose {p2}")
if p1 == p2:
    print("Tie")
elif (p1 == "rock" and p2 == "paper") or\
     (p1 == "paper" and p2 == "scissors") or\
     (p1 == "scissor" and p2 == "rock"):
     print("p2 wins")
else:
     print("p1 wins")
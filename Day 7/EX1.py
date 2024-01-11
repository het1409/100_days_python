
import random
from words import word_list


##word_list = ["Apple", "Banana", "Carrot", "Dog", "Elephant", "Fountain", "Guitar", "House", "Island", 
#             "Jazz", "Kangaroo", "Lighthouse", "Mountain", "Notebook", "Orange"]

word_choice = random.choice(word_list)
print(word_choice)

lives = 6
display = []
for letter in word_choice:
    #display += "_" 
    display = display + ["_"]
print(display)

end_game = False
while end_game == False:
    guess = input("guess a letter: ").lower()
  
    for position in range(len(word_choice)):
        letter = word_choice[position]
        if letter == guess:
            display[position] = letter
    if guess not in word_choice:
        lives = lives - 1
        print(f"Lives left is: {lives}")
        if lives == 0:
            end_game = True
            print(f"Exited. The word is {word_choice}")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("Complete")
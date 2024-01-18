from random import randint
easy_level = 10
hard_level = 5


#check if the guesses number is correct
def check(guess, answer, attempt):
    if guess > answer:
        print("Too High!")
        return attempt - 1
    elif guess < answer:
        print("Too low!")
        return attempt - 1
    else:
        print("MATCHED...")

#setting the difficulty

def set_level():
    level = input("Select level from 'easy' or 'hard': ").lower()
    if level == "easy":
        return easy_level
    else:
        return hard_level

def game():  
    print("Number Guessing game")
    print("Guessing Number...")

    answer = randint(1, 100)
    turns = set_level()
    print(f"{turns} attempts left")

    guess = 0
    while guess != answer:
        print(f"{turns} turns remaining")
    #user's Input
        guess = int(input("Guess a number: "))

        turns = check(guess, answer, turns)
        if turns == 0:
            print("no attempts left")
game()
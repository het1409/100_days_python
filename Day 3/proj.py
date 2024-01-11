#Treasure Island

print("Welcome to Treasure island")

c1 = input("L or R")
#c2 = input("S or W")
#c3 = input("Red, Blue or Yellow")

if c1 == "L":
    c2 = input("S or W")
    if c2 == "W":
        c3 = input("R, Y or B door")
        if c3 == "R":
            print("Game Over!")
        elif c3 == "Y":
            print("You Win!")
        elif c3 == "B":
            print("Game Over!")
        else:
            ("Wrong door. Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")
        


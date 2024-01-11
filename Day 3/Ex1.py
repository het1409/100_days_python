height = int(input("Enter your height in cm: "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Please pay £5.")
    elif age == 12 or age <=18:
        bill = 7
        print("Pay £7.")
    else:
        bill = 12
        print("pay £12.")

    photo = input("Wnat photo? Y or N: ")
    if photo == "Y":
        #pays extra 3£
        bill = bill + 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

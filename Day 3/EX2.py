year = int(input())

if year % 4 == 0 and year % 100!= 0:
    print("Leap year")
else:
    print("Not leap year")

'''if year is cleanly divisible by 4 and not divisible by 100, 
then it is a leap year else, it is not a leap year'''
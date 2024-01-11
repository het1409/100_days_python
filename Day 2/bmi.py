'''Program to caluculate BMI
BMI = weight / height**2 '''

height = input()
weight = input()

#Convert weight into float
new_h = float(height)
#Convert height into int
new_w = int(weight)

#Calculate BMI
BMI = new_w / (new_h * new_h)
print(int(BMI))

#formula for BMI = weight / height**2.
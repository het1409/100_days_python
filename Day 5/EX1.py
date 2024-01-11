# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0
for heights in student_heights:
  total_height = total_height + heights
print(f"total heights = {total_height}")

total_students = 0
for student in student_heights:
  total_students = 1 + total_students
print(f"total students = {total_students}")

avg_height = round(total_height / total_students)
print(f"avg height = {avg_height}")
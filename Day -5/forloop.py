fruits = ["Apple", "Banana", "Pear"]
for fruit in fruits :
    print(fruit)
    print(fruit + " Pie")
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
total_height = 0
for height in student_heights:
   total_height += height
# print(f"total height = {total_height}")

numbers_of_student = 0
for numbers in student_heights:
  numbers_of_student += 1
# print(f"Numbers of Student {numbers_of_student} \n")

#average
avg = total_height/numbers_of_student
print(round(avg))

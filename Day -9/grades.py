student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
for grade in student_scores:
  # print(grade)
  # print(student_scores[grade])
  if student_scores[grade] > 90 and student_scores[grade] <= 100:
    student_scores[grade] = "Outstanding"
  elif student_scores[grade] > 80 and student_scores[grade] < 90:
    student_scores[grade] = "Exceeds Expectations"

  elif student_scores[grade] > 70 and student_scores[grade] < 80:
    student_scores[grade] = "Acceptable"

  elif student_scores[grade] <70 :
    student_scores[grade] = "Fail"

  
  student_grades = student_scores
  

    

# 🚨 Don't change the code below 👇
print(student_grades)
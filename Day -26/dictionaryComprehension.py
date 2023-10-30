#new_dict = {new_key : new_value for item in list}
#new_dict = {new_key: new_value for (key,value) in dict.items()}
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# student_scores ={
#     "Alex": 90,
#     "Beth": 85,
#     "Caroline": 76,
#     "Dave": 92,
#     "Eleanor": 81,
#     "Freddie": 84
# }

student_scores = {student:random.randint(1, 100) for student in names}
passed_students = {student: score for student, score in student_scores.items() if score >= 60}
print(passed_students)
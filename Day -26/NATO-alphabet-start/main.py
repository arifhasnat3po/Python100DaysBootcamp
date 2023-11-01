student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# for (index, row) in student_data_frame.iterrows():
#     print("Student Name : ",row["student"])


import csv
import pandas as pd
nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter : row.code for (index, row) in nato_alphabet.iterrows()}
#    new_dict += {row.letter : row.code}
    # print(row.letter)
    # print(row.code)
print(new_dict)
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter any word: ").upper()
phonetic_list = [new_dict[letter] for letter in user_input if letter in new_dict]

print("Phonetic List:", phonetic_list)


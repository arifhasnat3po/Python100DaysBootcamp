# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combine_name = name1 + name2
lower_case_name = combine_name.lower()
true_or_false = lower_case_name.count("t") + lower_case_name.count(
    "r") + lower_case_name.count("u") + lower_case_name.count("e")
# print(lower_case_name)
# print(true_or_false)

love_for_true = str(true_or_false)
# print(type(love_for_true))

being_love = lower_case_name.count("l") + lower_case_name.count("o")+ lower_case_name.count("v")+ lower_case_name.count("e")

for_love = str(being_love)

love_score = love_for_true + for_love

# print(love_score)

score = int(love_score)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50 :
  print(f"Your score is {score}, you are alright together.")

else:
  print(f"Your score is {score}.")
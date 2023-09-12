# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(names)
# name_list = names
# print(len(names))
# lenth_of_list = len(names)
# # print(lenth_of_list)
# random_number = random.randint(0, lenth_of_list -1)
# pay_by = names[random_number]
# # print(random_number)
pay_by = random.choice(names)
print(f"{pay_by} is going to buy the meal today!")
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input >= 3 or user_input < 0:
 print("Please enter a valid number")
if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)
#Write your code below this line 👇
#for computer
random_value = random.randint(0,2)
print("Computer chose:\n")
if random_value == 0:
  print(rock)
elif random_value == 1:
  print(paper)
elif random_value == 2:
  print(scissors)

#comparing the string
if user_input == random_value :
  print("It's a tie, Try again :0\n")
elif user_input == 0 and random_value == 2:
  print("You Win\n")
elif user_input == 2 and random_value == 0:
  print("you Lose\n")


elif user_input == 2 and random_value == 1:
  print("You Win\n")
elif user_input == 1 and random_value == 2:
  print("you Lose\n")


elif user_input == 1 and random_value == 0:
  print("You Win\n")
elif user_input == 0 and random_value == 1:
  print("you Lose\n")
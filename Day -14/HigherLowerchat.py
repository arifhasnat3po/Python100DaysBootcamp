import random
from art import logo, vs
from game_data import data

def display_comparison(dictionary):
    all_values = [str(value) for value in dictionary.values()]
    print(f"Compare: {all_values[0]}, a {all_values[2]}, from {all_values[3]}")

def play_game():
    score = 0  # Initialize the user's score
    while True:
        print(logo)
        first_dictionary = random.choice(data)
        display_comparison(first_dictionary)
        print(vs)
        second_dictionary = random.choice(data)
        display_comparison(second_dictionary)

        first_follower_value = first_dictionary["follower_count"]
        second_follower_value = second_dictionary["follower_count"]

        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

        if (user_input == "a" and first_follower_value > second_follower_value) or \
           (user_input == "b" and second_follower_value > first_follower_value):
            score += 1
            print(f"Correct! Your current score is {score}")
        else:
            print(f"Sorry, that's wrong. Your final score is {score}")
            break  # Exit the loop when the user loses

play_game()

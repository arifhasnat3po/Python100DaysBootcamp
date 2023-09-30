import random
from art import logo, vs
from game_data import data

def display_comparison(dictionary):
    all_values = [str(value) for value in dictionary.values()]
    print(f"Compare: {all_values[0]}, a {all_values[2]}, from {all_values[3]}")

def play():
    score = 0
    is_game_over = False
    while not is_game_over:
        print(logo)
        first_dictionary = random.choice(data)
        display_comparison(first_dictionary)
        print(vs)
        second_dictionary = random.choice(data)
        display_comparison(second_dictionary)

        # Access the "follower_count" key in the selected dictionary
        first_follower_value = first_dictionary["follower_count"]
        second_follower_value = second_dictionary["follower_count"]



        user_input = input("Who has more followes? Type 'A' or 'B': ")
        A = first_follower_value
        B = second_follower_value
        if user_input == "A" and first_follower_value > second_follower_value:
            score += 1
            print(f"Correct! Your current score is {score}")
            
        elif user_input == "B" and second_follower_value > first_follower_value:
            score += 1
            print(f"Correct! Your current score is {score}")
            
        else:
            print(f"Sorry, that's wrong. Your final score is {score}")
            is_game_over = True
play()
            
        
    
    


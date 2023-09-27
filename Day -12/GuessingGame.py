from art import logo
print(logo)
import random  # we need this to generate a random number.

print("Welcome to the Number Guessing Game!")

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, answer, turns):
    
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")
        
def set_difficulty():
    level = input("Set difficulty. Type 'easy' or 'hard' : ").lower()
    if level == "easy":
        return EASY_LEVEL
    
    else:
        return HARD_LEVEL
    
    
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"psst, The answer is {answer}")
    guess = int(input("Make a guess: "))
    turns = set_difficulty()
    check_answer(guess, answer, turns)
    # while turns != 0:
    #     guess = int(input("Make a guess: "))
    #     turns = check_answer(guess, answer, turns)
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns ==0:
            print("You've run out of guesses, you lose.")
            return
        else:
            print("Guess again")
                

game()



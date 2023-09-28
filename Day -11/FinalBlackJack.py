from art import logo
import random
from replit import clear


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
      
  return random.choice(cards)


 
def calculate_score(cards):


  if sum(cards) == 21 and len(cards) ==2:
    return 0

  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)
  

def compare (user_score,computer_score):

  if user_score > 21 and computer_score >21:
    return "You went over. You lose :( "

  elif user_score == computer_score:
    return "Match Draw"
  elif user_score == 0:
    return " You win with a Blackjack "

  elif computer_score == 0:
    return "You lose , opponent has Blackjack "

  elif user_score > 21:
    return "You went over you lose"

  elif computer_score > 21:
    return "You win, Opponent went over "

  elif user_score > computer_score:
    return "You win "

  else:
    return "You lose"

def play_game():
  print(logo)
  print("Welcome to Blackjack!")
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  
    
  for _ in range(2):
    user_cards.append(deal_cards())
  
  computer_cards = []
  for _ in range(2):
    computer_cards.append(deal_cards())


  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score  = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, Current Score: {user_score} ")
    # print(f" Computer cards: {computer_cards}, Current Score: {computer_score} ")
    print(f" Computer's first card: {computer_cards[0]} ")
    
    
    
    # print(compare(user_score,computer_score))
    if user_score > 21  or computer_score == 0 or user_score == 0 :
      is_game_over = True

    else:
      user_input = input("Do you want to get another card type 'y' for yes or 'n' for no : ").lower()
      if user_input == 'y':
        user_cards.append(deal_cards())
      else:
        is_game_over = True
  while computer_score !=0 and computer_score < 17:
    computer_cards.append(deal_cards())
    computer_score = calculate_score(computer_cards)
    
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  clear()
  play_game()




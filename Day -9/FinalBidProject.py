from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
# def user_info(user_name,user_bid):
# user_name = input("what is you name? : ")
# user_bid = int(input("How much do you want to bid? :$"))

# user = input("Is there any other bidder who wants to bid? if 'yes' than type y otherwise type n \n").lower()

bid = {}
bidding_finish = False
def find_highest_bider(biding_record):
  highest_bid = 0
  winner = ""
  for bider in biding_record:
    bid_amount = biding_record[bider]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bider
  print(f"The winner is {winner} with a bid of ${highest_bid}")
      # print(highest_bid)

# user = input("Is there any other bidder who wants to bid? if 'yes' than type y otherwise type n \n").lower()
# if user == "y":

while not bidding_finish:
  user_name = input("what is you name? : ")
  user_bid = int(input("How much do you want to bid? :$"))
  bid[user_name] = user_bid
  user = input("Is there any other bidder who wants to bid? if 'yes' than type y otherwise type n \n").lower()

  if user == 'y':
    clear()

  elif user == 'n':
    bidding_finish = True
    find_highest_bider(bid)

# elif user == "n":
#   bidding_finish = True
  


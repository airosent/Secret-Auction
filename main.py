from replit import clear
from art import logo

print(logo)
print("Welcome to the Secret Auction!")

user_storage = {}
bidding_finished = False

def find_highest(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with the highest bid of ${highest_bid}.")

while not bidding_finished:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  user_storage[name] = bid
  other_bidders = input("Are there any other bidders? (type 'yes' or 'no')\n")
  if other_bidders == 'no':
    bidding_finished = True
    find_highest(user_storage)
  elif other_bidders == 'yes':
    clear()
  else:
    bidding_finished == True
 



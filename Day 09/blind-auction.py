from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the online bid")

bid_run = True
bid_note = {}

while bid_run:
  user_name = str(input("Please give your name: "))
  bid_price = float(input("What is your bid amount: $"))
  bid_note[user_name] = bid_price
  another_bid = str(input("Any other user wants to bid: ")).lower()
  if another_bid == "yes":
    clear()
    # continue
  else:
    bid_run = False

max_bid = 0
max_bidder = ""
for key in bid_note:
  print(key, '->', bid_note[key])
  if bid_note[key] > max_bid:
    max_bid = bid_note[key]
    max_bidder = key

print(f"The winner is {max_bidder} and the bid amount is {max_bid}")
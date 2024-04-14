art ='''                              
                                          88                          
                                    ,d    ""                          
                                    88                               
,adPPYYba, 88       88  ,adPPYba, MM88MMM 88  ,adPPYba,  8b,dPPYba,   
""     `Y8 88       88 a8"     ""   88    88 a8"     "8a 88P'   `"8a  
,adPPPPP88 88       88 8b           88    88 8b       d8 88       88  
88,    ,88 "8a,   ,a88 "8a,   ,aa   88,   88 "8a,   ,a8" 88       88  
`"8bbdP"Y8  `"YbbdP'Y8  `"Ybbd8"'   "Y888 88  `"YbbdP"'  88       88  
                                                                      
'''
print(art)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  
  
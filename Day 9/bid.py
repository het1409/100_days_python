
all_bids = {}

def top_bid(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(highest_bid)
bid_finshed = False
while not bid_finshed:
    name = input("Enter your name: \n")
    bid = int(input("Enter Bid amount: \n"))
    all_bids[name] = bid
    n2 = input("Add more name? Yes/No .")
    if n2 == "No":
        bid_finshed = True
        top_bid(all_bids)

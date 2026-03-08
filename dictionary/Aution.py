
#ToDO -1 Ask the user for input
#TODO -2 Save the data in dictionary
#ToDO -3: Whether if new bids needs to be Added
import art


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid} ")

bids ={}
continue_bidding = True
while continue_bidding:
    name = input("What is your name ?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'No'. \n").lower()
    if should_continue == "no":
        continue_bidding=False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n"*30)


#TODO -4 : Compare bids in dictionary

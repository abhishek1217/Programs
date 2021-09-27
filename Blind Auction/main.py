from replit import clear
from art import logo
print(logo)
auction_dict = {}
end_of_loop = True

while end_of_loop:

	name = input("What is your name? ")
	bid = int(input("What is your bid? $"))
	auction_dict[name] = bid
	end = input("Are there any other bidders? Type yes or no\n").lower()
	if end == "no":
		end_of_loop = False
	elif end == "yes":
		clear()

max = -1
max_name = ""
for key in auction_dict:
	if auction_dict[key] > max:
		max = auction_dict[key]
		max_name = key

print(f"The winner is {max_name} with a bid of ${max}")
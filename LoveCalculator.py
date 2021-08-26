print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name = name1 + name2
name =name.lower()
true = name.count('t') + name.count('r') +  name.count('u') + name.count('e')
love = name.count('l') + name.count('o') +  name.count('v') + name.count('e')
total_score = int(str(true) + str(love))
if total_score < 10 or total_score > 90:
	print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
	print(f"Your score is {total_score}, you are alright together.")
else:
	print(f"Your score is {total_score}.")



year = int(input("Which year do you want to check? "))
# https://www.youtube.com/watch?v=xX96xng7sAE
# Leap year if divsible by 4
# Not a leap  year if divisible by 100 but is a leap year if divisible by 400
if year % 100 == 0:
	if year % 400 == 0:
		print("Leap")
	else:
		print("Not Leap")
elif year % 4 == 0:
	print("Leap")
else:
	print("Not Leap")

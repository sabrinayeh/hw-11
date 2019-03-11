
import random

answer = random.randint(1, 10)

while True: 
	
	try:

		user_input = int(input("I'm thinking of a number between 1 and 10. Please guess what it is:"))

	except ValueError:
		print("Oh That is NOT a number, Bart!")

		continue

	if user_input > answer:
		print("That is too high!")
	elif user_input < answer:
		print("That is too low!")
	else:
		print("That's it! You win!")
		
		break


"""
I'm thinking of a number between 1 and 10.
Please guess what it is:
> Eat my shorts!
D'oh! That is NOT a number, Bart!
Please guess what it is:
> Ay, caramba!
D'oh! That is NOT a number, Bart!
Please guess what it is:
> 5
That is too low!
Please guess what it is:
> 8
That's it! You win!

"""
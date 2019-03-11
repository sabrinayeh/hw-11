
import random

answer = random.randint(1, 10)

while True: 
	user_input = int(input("I'm thinking of a number between 1 and 10. \n Please guess what it is:"))
	if user_input > answer:
		print("That is too high!")
	elif user_input < answer:
		print("That is too low!")
	else:
		print("That's it! You win!")
		break


"""
Higher than the answer: print That is too high!.
Lower than the answer: print That is too low!.
Exactly the answer: print That's it! You win!.


I'm thinking of a number between 1 and 10.
Please guess what it is:
> 4
That is too low!
> 8
That is too high!
> 6
That's it! You win!

"""
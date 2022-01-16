# Importing random module
import random
import time


# Choosing random integer
random_number = random.randint(0,2)

 
print("\n")
print("Please choose among rock , paper and scissor")
print("\n")

# Taking users input
user_input = input("Enter your choice: ")

# Assigning values to variables
hand0 = "rock"
hand1 = "paper"
hand2 = "scissor"


# Draw case scenario starts
if random_number == 0 and user_input == hand0 :
	print("Your Decision: " + user_input)
	print("Computer decision: " + hand0) 
	print("It's a draw")

elif random_number == 1 and user_input == hand1 :
	print("Your Decision: " + user_input)
	print("Computer decision: " + hand1)
	print("It's a draw")	

elif random_number == 2 and user_input == hand2 :
	print("Your Decision: " + user_input)
	print("Computer decision: " + hand2)	
	print("It's a draw")
# Draw case scenario ends


# Win case scenario starts
elif user_input == hand0 and random_number == 2:
	print("Your Decision: " + user_input)
	print("Computer decision: " + hand2)
	print("You win")

elif user_input == hand1 and random_number == 0:
	print("Your Decision: " + user_input)
	print("Computer decision: " + hand0)
	print("You win")	

elif user_input == hand2 and random_number == 1:
	print("Your Decision: " + user_input)
	print("Computer decision: " + hand1)
	print("You win")
# Win case scenario ends


# Lose case scenario starts
elif user_input == hand2 and random_number == 0:
	print("Your Decision: " + user_input)
	print("Computer decision: " + hand0)
	print("You Lose")

elif user_input == hand1 and random_number == 2:
	print("Your Decision: " + user_input)
	print("compuer decision: " + hand2)
	print("You Lose")

elif user_input == hand0 and random_number == 1:	
	print("Your Decision: " + user_input)
	print("Computer decision: " + hand1)
	print("You lose")
# Lose case scenario ends

print("\n")
response = input("Press 'y' to play again or 'n' to exit: ")


while response != 'n':
	if response == 'y':
		# Choosing random integer
		random_number = random.randint(0,2)
 
		print("\n")
		print("Please choose among rock , paper and scissor")
		print("\n")
		# Taking users input
		user_input = input("Enter your choice: ")
		# Assigning values to variables
		hand0 = "rock"
		hand1 = "paper"
		hand2 = "scissor"

			# Draw case scenario starts
		if random_number == 0 and user_input == hand0 :
			print("Your Decision: " + user_input)
			print("Computer decision: " + hand0) 
			print("It's a draw")

		elif random_number == 1 and user_input == hand1 :
			print("Your Decision: " + user_input)
			print("Computer decision: " + hand1)
			print("It's a draw")	
		elif random_number == 2 and user_input == hand2 :
			print("Your Decision: " + user_input)
			print("Computer decision: " + hand2)	
			print("It's a draw")
		# Draw case scenario ends

		# Win case scenario starts
		elif user_input == hand0 and random_number == 2:
			print("Your Decision: " + user_input)
			print("Computer decision: " + hand2)
			print("You win")
		elif user_input == hand1 and random_number == 0:
			print("Your Decision: " + user_input)
			print("Computer decision: " + hand0)
			print("You win")	
		elif user_input == hand2 and random_number == 1:
			print("Your Decision: " + user_input)
			print("Computer decision: " + hand1)
			print("You win")
		# Win case scenario ends


			# Lose case scenario starts
		elif user_input == hand2 and random_number == 0:
			print("Your Decision: " + user_input)
			print("Computer decision: " + hand0)
			print("You Lose")

		elif user_input == hand1 and random_number == 2:
			print("Your Decision: " + user_input)
			print("compuer decision: " + hand2)
			print("You Lose")

		elif user_input == hand0 and random_number == 1:	
			print("Your Decision: " + user_input)
			print("Computer decision: " + hand1)
			print("You lose")
		# Lose case scenario ends

	print("\n")
	response = input("Press 'y' to play again or 'n' to exit: ")

time.sleep(2)
print("\n")
print("----- Game Over -----")
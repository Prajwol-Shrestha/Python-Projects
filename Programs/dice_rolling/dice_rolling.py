import random

def again():
	print("----- Rolling the dice ------")
	print("\n")
	dice_num = random.randint(1,6)
	print("\n")
	print("You got " + str(dice_num))
	
	while dice_num in rollagain:
		print("\n")
		print("Woah! You got a six. You get to roll again")
		print("---Rolling Again--")
		dice_num = random.randint(1,6)
		print("\n")
		print("You got " + str(dice_num))

def first():
	print("\n")
	ask = input("Roll the dice? : ")
	if ask in response:
		print("\n")
		print("----- Rolling the dice ------") 
		dice_num = random.randint(1,6)
		print("\n")
		print("You got " + str(dice_num))
		while dice_num in rollagain:
			print("\n")
			print("Woah! You got a six. You get to roll again")
			print("---Rolling Again--")
			dice_num = random.randint(1,6)
			print("\n")
			print("You got " + str(dice_num))
	elif ask not in response:
		exit()

response = ["yes", "y" or "Yes" or "Y"]
rollagain = [6]

first()
print("\n")
ask = input("Do you want to roll the dice again? : ")


while ask in response:
	again()
	print("\n")
	ask = input("Do you want to roll the dice again? : ")
print("\n")
print("------Exiting Program-----")
	
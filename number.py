import random

print("welcome to the guessing game!")
print("I'm thinking of a number between 1 to 20")

the_number = random.randint (1,20)
guess = True
Tries = 0

while guess != the_number:
	guess =int(input("take a guess"))
	Tries += 1
	if guess > the_number:
		print("lower ...")
	elif guess < the_number:
		print("higher ...")

print("You guessed it CONGRATS, the number was", the_number)

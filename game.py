import random

# A list of words that
potential_words = ["new york city"]

word = random.choice(potential_words)
# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

insert = potential_words

# Make it a list of letters for someone to guess
current_word = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"] # TIP: the number of letters should match the word

for letter in potential_words:
    word.append("-")
# Some useful variables
guesses = [10]
maxfails = 10
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")

	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	print(current_word)

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")

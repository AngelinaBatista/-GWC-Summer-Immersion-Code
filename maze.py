start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()
if user_input == "left":
    print("You decide to go left and...") # Update to match your story.
    print("you touched the wall")
    print("GAME OVER")
    # Continue code to finish story.
elif user_input == "right":
    print("You choose to go right and ...") # Update to match your story.
    print("You run into a dragon")
    user_input = input("Type 'right' to go right or 'left' to go left")

if user_input == 'right':
    print("OH NO you have been attacked by birds!")
    print("you start running away and you come across two doors")
    user_input = input("Type 'right' to go right or 'left' to go left")

    if user_input == "right":
        print("It's a dead end")
        print("GAME OVER")

    if user_input == "left":
        print("YOU MAKE IT BACK TO YOUR BED")
        print("CONGRATS")

elif user_input == 'left':
    print("You start walking down a quiet dark road")
    print("You see a fox, it starts to walk away ")
    user_input = input("Do you follow the fox 'right' or continue on left?")

if user_input == "left":
    print("You continue down the path and it starts to get darker and colder")
    print("It's a never ending path and you die")
    print("GAME OVER")

elif user_input == "right":
    print("YOU MADE IT BACK TO YOUR BED")
    print("CONGRATS")
    

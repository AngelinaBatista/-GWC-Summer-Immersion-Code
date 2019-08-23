print("What will your dinner be?")

import random
first = ("chips", "fries", "onion rings", "salads")
second = ("burger", "chicken tenders", "burrito", "tacos")
third = ("ice cream", "apple pie", "brownie", "cake")
firrst = random.choice(first)
seccond = random.choice(second)
thiird = random.choice(third)
name = (firrst + " " + seccond + " " + thiird
)
print("Your dinner is: " + name)

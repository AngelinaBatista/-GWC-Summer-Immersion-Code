#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dic.txt","r")
text = f.read().strip().split()
print("Can your password survive a dictionary attack?")

for i in range(3):
    x = input("Type in a trial password: ")
#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords

#Write logic to see if the password is in the dictionary file below here:
    if x in text:
        print("The password: " + "''" + (x) + " it's too weak. ")
        print("YoUVe beEn HaCKEd HAhaahaaAha")

    else:
        print("WOw you have a really strong password")

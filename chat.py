# --- Define your functions below! ---
# --- Put your main program below! ---
def intro():
    print("Hello my name is Chatty, let's talk!")
    print("Type something and hit enter.")

def greet(answer):
    if answer == "hi":
        name(answer)
    else:
        cool()

def name(answer):
    print("how are you?")
#    if answer == "good":
#        cool()
#    else:
#        ok()


#ef woah(answer):
    #print("do you want to see a poem?")
    ##if answer == "yes":
    #    print("To those whom I've fought with and to those I don't know your name, we fought by one another. You did not die in vain.")
    #else:
    #    ok()
def ok():
    print("oh ok then")

def bad():
    print("Aww I'm sorry")
    woah()



def cool():
    print("That's cool")


def main():
    intro()


    while True:
        answer = input("(What will you say?) ")
        greet(answer)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()

# ------------------------------------------------------
#       Name: Madison Milla
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Read text from user until secret word is used,
        Check to see if user used secret word; if so, print "you used the secret word".
        If the user inputs text with the word "food" or "Food", print "you used the word "food" or "Food"!
        If user does not use secret word or words, it should print "Try again" and run loop again.
        """
    while True: # while loop since this depends on an unpredictable condition
        result = input("Give me a sentence: ")
        
        if secret_word in result:
            print("You used the secret word!")
            break
        elif "dog" in result or "Dog" in result:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        else:
            print("Try again")

# Task 2
def check_greater():
    """ Get 2 integers from user and compare
        If first int is greater than second, print 'First is greater'
        If second is greater than first, print 'Second is greater'
        If ints are equal, print 'Try again'
        """
    while True:
        result1 = input("Give me an integer: ")
        result2 = input("Give me another integer: ")
        
        if result1 > result2:
            print("First is Greater")
            print("Done")
            break
        elif result1 < result2:
            print("Second is Greater")
            print("Done")
            break
        else:
            print("Try again")
        
# Task 3
def get_special_numbers():
    """Count to 40 every third number
        If even, skip and continue
        If not multiple of 3, skip and continue
        If multiple of 5, skip and continue
        """
    for i in range (1,41):
        if i % 2 == 0:
            continue
        if i % 3 != 0:
            continue
        if i % 5 == 0:
            continue
        else:
            print (i)
        
# Task 4.a
def my_for_loop():
    """ Ask for a string 2<=string<=5
        if letter is a vowel, print letter = vowel
        if letter is a consonant, print letter = consonant
        """
    text = input("Give me a string: ")
    
    if not (2 <= len(text) <=5) or " " in text: # check length and spaces
        print("bad word")
        return
    
    vowels = "a,e,i,o,u,A,E,I,O,U"
    
    for letter in text:
        if letter in vowels:
            print(f"{letter} is a vowel")
        else:
            print(f"{letter} is a consonant")
    
# Task 4.b
def my_while_loop():
    """ Offer three choices where use inputs one of three letters
        if user selects a, repeat
        if user selects b, print Goodbye
        if user selects c, exit
        """
    while True:
        choice = input("Choose an option: a, b, or c: ")
        
        if choice == "a":
            continue
        elif choice == "b":
            print("Goodbye")
            break
        elif choice == "c":
            sys.exit()
        else:
            print("try again")

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")

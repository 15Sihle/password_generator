import random
import sys

def password_generator():
    
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["1","2","3","4","5","6","7","8","9", "0"]
    symbols = ["!", "@", "#", "%", "&", "*", "?", "/", ">", "<"]

    new_passsword = []
    
    try:

        letters_input = int(input("how many letters do you want in your password "))
        numbers_input = int(input("how many numbers do you want in your password "))
        symbols_input = int(input("how many symbols do you want in your password "))


    except ValueError:
        print("strictly insert a number, nothing else")
        sys.exit(1)

    if letters_input <= 0:
        print("strictly insert a number bigger than 0")
        sys.exit(1)

    if numbers_input <= 0:
        print("strictly insert a number bigger than 0")
        sys.exit(1)

    if symbols_input <= 0:
        print("strictly insert a number bigger than 0")
        sys.exit(1)
    
    for i in range(letters_input):
        new_passsword.append(random.choice(letters))

    for i in range(numbers_input):
        new_passsword.append(random.choice(numbers))

    for i in range(symbols_input):
        new_passsword.append(random.choice(symbols))
    
    print()
    print("Your new password is: ")
    random.shuffle(new_passsword)
    print("".join(new_passsword))

password_generator()

        

        
        
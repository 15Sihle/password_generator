import random
import string

class PasswordGenerator:
    def __init__(self):
        pass

    def generate_password(self, length, use_uppercase, use_lowercase, use_digits, use_symbols):
        uppercase_letters = string.ascii_uppercase
        lowercase_letters = string.ascii_lowercase
        digits = string.digits
        symbols = string.punctuation

        characters = ""
        if use_uppercase:
            characters += uppercase_letters
        if use_lowercase:
            characters += lowercase_letters
        if use_digits:
            characters += digits
        if use_symbols:
            characters += symbols
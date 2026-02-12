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

        if characters:
            password = ''.join(random.choice(characters) for _ in range(length))
            return password
        else:
            return "Character set not selected."
        
    def save_password_to_file(self, password, filename):
        with open(filename, "w") as file:
            file.write(password)

    def main(self):
        print("Random Password Generator")

        length = int(input("Password Length: "))

        use_uppercase = input("Use Uppercase Letters? (Y/N): ").lower() == "y"
        use_lowercase = input("Use Lowercase Letters? (Y/N): ").lower() == "y"
        use_digits = input("Use Digits? (Y/N): ").lower() == "y"
        use_symbols = input("Use Symbols? (Y/N): ").lower() == "y"

        password = self.generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)

        print("\nGenerated Password:", password)

        save_to_file = input("Save the password to a file? (Y/N): ").lower() == "y"
        if save_to_file:
            filename = input("Enter the filename: ")
            self.save_password_to_file(password, filename)
            print(f"Password saved to {filename}")

if __name__ == "__main__":
    password_generator = PasswordGenerator()
    password_generator.main()


        

        
        
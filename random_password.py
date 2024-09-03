import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    character_set = string.ascii_lowercase
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return

        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Invalid input! Please enter numeric values for the password length.")

main()

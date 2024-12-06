import random
import string
# Paaswaord generator 

def generate_password(length, use_letters, use_digits, use_symbols):
    character_set = ""
    if use_letters:
        character_set += string.ascii_letters
    if use_digits:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    if not character_set:
        raise ValueError("No character types selected.")
    return ''.join(random.choice(character_set) for _ in range(length))

def main():
    print("Random Password Generator")
    try:
        length = int(input("Enter password length: "))
        use_letters = input("Include letters? (yes/no): ").strip().lower() == "yes"
        use_digits = input("Include digits? (yes/no): ").strip().lower() == "yes"
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"
        if length <= 0:
            raise ValueError("Password length must be positive.")
        password = generate_password(length, use_letters, use_digits, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

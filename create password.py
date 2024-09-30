#create secuew password
#Lwazi Somtsewu


import random
import string

def generate_password(length=12):
    # Define the character sets to choose from
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters
    
    # Ensure the password contains at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    length = int(input("Enter the desired password length (minimum 8): "))
    if length < 8:
        print("Password length should be at least 8 characters.")
    else:
        generated_password = generate_password(length)
        print("Generated Password:", generated_password)

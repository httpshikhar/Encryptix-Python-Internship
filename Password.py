import string
import random

def generate_password(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password length is at least 6 characters
    if length < 8:
        return "Password length should be at least 6 characters."
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password


# Get the length of the password from the user
try:
    length = int(input("Enter the desired length for the password: "))
except ValueError:
    print("Please enter a valid number.")
    
    # Generate the password
password = generate_password(length)
    
    # Print the password
print(f"Generated password: {password}")

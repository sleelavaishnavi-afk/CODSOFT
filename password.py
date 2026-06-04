import random
import string
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
special_characters = string.punctuation
characters = lowercase + uppercase + numbers + special_characters
length = int(input("Enter password length: "))
password = ""
for i in range(length):
    password += random.choice(characters)
print("Generated Password:", password)
import random

# Create a list of characters (uppercase and lowercase English alphabets)
words = []
for i in range(26):
    words.append(chr(65 + i))  # Append uppercase letters (A-Z)
    words.append(chr(97 + i))  # Append lowercase letters (a-z)

# Function to generate a random password
def generate_password(length, words):
    password = ""
    for _ in range(length):
        index = random.randint(0, 51)  # Random index between 0 and 51 (52 letters in total)
        password += words[index]
    return password

# Get the length of the password from the user
length = int(input("Enter the length of password: "))
password = generate_password(length, words)

# Print the randomly generated password
print(f'The randomly generated password is: {password}')

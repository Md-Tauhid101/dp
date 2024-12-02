# Q. Write a Python program that simulates a brute-force attack on a password by trying out
# all possible character combinations.

from itertools import product

def brute_force_attack(password):
    # Characters that might be in the password
    words = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_length = len(password)
    count = 0  # Variable to keep track of the number of combinations tried

    # Looping till the length of the password
    for r in range(1, max_length + 1):
        # Looping through all combinations of characters
        for combo in product(words, repeat=r):
            count += 1
            # Checking if the current combination matches the password
            if ''.join(combo) == password:
                print(''.join(combo), "is found after", count, "combinations")
                return  # Exit the function once the password is found

# Taking input from the user
password = input("Enter the password: ")
brute_force_attack(password)

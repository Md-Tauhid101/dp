# Opening file and writing usernames and passwords in it
with open('info.txt', 'w') as f:
    data = [('user1', 'password'), ('user2', 'pass1234'), ('user3', 'djfhdgaohfoanf')]
    for username, password in data:
        f.write(f"{username},{password}\n")

# Reading and printing the file contents
with open('info.txt', 'r') as f:
    print(f.read())

# Importing necessary libraries
import hashlib
import requests

# Opening file for reading data
with open('info.txt', 'r') as f:
    # Iterating over each username and password
    for line in f:
        # Splitting the username and password into two parts
        user, password = line.strip().split(',')

        # Converting the password to hash and hexadecimal in uppercase
        pass_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

        # Calling API to get the leaked passwords by matching the first 5 letters of the password hash
        response = requests.get(f'https://api.pwnedpasswords.com/range/{pass_hash[:5]}')

        # Checking the status of the response
        if response.status_code == 200:
            # Splitting the matching hashes
            hashes = response.text.splitlines()
            count = 0  # Keeping track of how many times the password is leaked

            # Iterating through all matching hashes
            for hash_suffix in hashes:
                # Password is leaked if the password hash matches completely
                if hash_suffix.split(':')[0] == pass_hash[5:]:
                    count += 1
                    print(f'Password for user {user} has been leaked')
                    break

            if count == 0:
                print(f'Password for user {user} has not been leaked')
        else:
            # Cannot search the password if response status is not 200
            print("Cannot search for password")

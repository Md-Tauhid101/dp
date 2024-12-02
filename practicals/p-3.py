import hashlib

def hash_password(password: str) -> str:
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    # Update the hash object with the bytes of the password string
    sha256_hash.update(password.encode('utf-8'))
    # Get the hexadecimal representation of the hash
    hashed_password = sha256_hash.hexdigest()
    return hashed_password

if __name__ == "__main__":
    # Input password from user
    user_password = input("Enter your password: ")
    # Hash the password
    hashed_password = hash_password(user_password)
    # Print the hashed password
    print(f"SHA-256 hashed password: {hashed_password}")
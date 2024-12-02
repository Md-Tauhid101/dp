def encrypt(text, key):
    # Create a matrix to store the rail pattern
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    down_dir = False
    row, col = 0, 0

    # Fill the rail matrix with the characters in zigzag pattern
    for i in range(len(text)):
        if row == 0 or row == key - 1:
            down_dir = not down_dir
        rail[row][col] = text[i]
        col += 1

        if down_dir:
            row += 1
        else:
            row -= 1

    # Construct the encrypted text by reading the matrix row by row
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)


def decrypt(cipher, key):
    # Create a matrix to store the rail pattern
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    down_dir = None
    row, col = 0, 0

    # Mark the zigzag pattern
    for i in range(len(cipher)):
        if row == 0:
            down_dir = True
        if row == key - 1:
            down_dir = False
        rail[row][col] = '*'
        col += 1

        if down_dir:
            row += 1
        else:
            row -= 1

    # Fill the matrix with the cipher text
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Read the matrix in zigzag pattern to decrypt
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            down_dir = True
        if row == key - 1:
            down_dir = False

        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1

        if down_dir:
            row += 1
        else:
            row -= 1

    return "".join(result)


# Main program
text = input("Enter the text to encrypt: ")
key = int(input("Enter the key for encryption: "))
encrypted = encrypt(text, key)
print(f'Encrypted text is: {encrypted}')
decrypted = decrypt(encrypted, key)
print(f'Decrypted text is: {decrypted}')

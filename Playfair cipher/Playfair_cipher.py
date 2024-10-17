import os
import logging
from setup.sprint import sprint
from setup.colors import c, r, ran, lr, lc, lg, g, ly, y
from setup.banner import banner, banner2, clear
import re

def generate_key_matrix(key):
    # Remove duplicates and create a key matrix
    key = key.upper()
    key = ''.join(sorted(set(key), key=key.index))
    
    # Prepare the matrix
    matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is usually omitted
    used_chars = set(key)
    
    # Append key letters to the matrix
    for char in key:
        matrix.append(char)
    
    # Append the remaining letters of the alphabet
    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
    
    # Reshape into a 5x5 matrix
    return [matrix[i:i + 5] for i in range(0, len(matrix), 5)]

def find_position(matrix, char):
    # Find the row and column of a character in the matrix
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def playfair_encrypt_decrypt(text, key, mode="encrypt"):
    # Prepare the key matrix
    matrix = generate_key_matrix(key)
    
    # Clean the text: remove non-alphabet characters, and handle 'J' by replacing with 'I'
    text = re.sub(r'[^A-Z]', '', text.upper().replace('J', 'I'))
    
    # Insert filler 'X' between duplicate letters in pairs
    prepared_text = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if (i + 1) < len(text) else 'X'
        if a == b:
            prepared_text.append(a + 'X')
            i += 1
        else:
            prepared_text.append(a + b)
            i += 2
    
    # If the length is odd, add an 'X' at the end
    if len(prepared_text[-1]) == 1:
        prepared_text[-1] += 'X'
    
    encrypted_text = []
    
    # Encryption and Decryption logic
    shift = 1 if mode == "encrypt" else -1
    
    for pair in prepared_text:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        
        if row1 == row2:
            # Same row: shift columns right (encrypt) or left (decrypt)
            encrypted_text.append(matrix[row1][(col1 + shift) % 5] + matrix[row2][(col2 + shift) % 5])
        elif col1 == col2:
            # Same column: shift rows down (encrypt) or up (decrypt)
            encrypted_text.append(matrix[(row1 + shift) % 5][col1] + matrix[(row2 + shift) % 5][col2])
        else:
            # Rectangle swap
            encrypted_text.append(matrix[row1][col2] + matrix[row2][col1])
    
    return ''.join(encrypted_text)

def main():
    os.system("clear")
    banner()
    # Input key and plaintext from user
    key = input("Enter the key: ")
    plaintext = input("Enter the plaintext: ")
    
    # Encrypt the plaintext
    ciphertext = playfair_encrypt_decrypt(plaintext, key, mode="encrypt")
    print(f"Ciphertext: {ciphertext}")
    
    # Decrypt the ciphertext
    decrypted_text = playfair_encrypt_decrypt(ciphertext, key, mode="decrypt")
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()

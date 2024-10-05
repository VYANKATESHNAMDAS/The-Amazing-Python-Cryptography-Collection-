import os
import logging
from setup.sprint import sprint
from setup.colors import c, r, ran, lr, lc, lg, g, ly, y
from setup.banner import banner, banner2, clear
import string

# Function to generate a cipher dictionary based on the key
def create_cipher_dict(key):
    letters = string.ascii_lowercase
    cipher_dict = {}
    
    # Create substitution dictionary
    for i in range(len(letters)):
        cipher_dict[letters[i]] = key[i]
    
    return cipher_dict

# Function to encrypt a message using monoalphabetic cipher
def encrypt_message(plain_text, key):
    cipher_dict = create_cipher_dict(key)
    encrypted_text = ''
    
    for char in plain_text.lower():
        if char in cipher_dict:
            encrypted_text += cipher_dict[char]
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    
    return encrypted_text

# Function to decrypt a message using monoalphabetic cipher
def decrypt_message(cipher_text, key):
    cipher_dict = create_cipher_dict(key)
    reverse_cipher_dict = {v: k for k, v in cipher_dict.items()}
    decrypted_text = ''
    
    for char in cipher_text.lower():
        if char in reverse_cipher_dict:
            decrypted_text += reverse_cipher_dict[char]
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged
    
    return decrypted_text

# Example usage
if __name__ == "__main__":
    os.system("clear")
    banner()
    print(" ")
    key = "qwertyuiopasdfghjklzxcvbnm"  # This is the key used for substitution
    plain_text = "Monoalphabetic"
    
    # Encrypt the message
    encrypted = encrypt_message(plain_text, key)
    print(f"Encrypted Message: {encrypted}")
    
    # Decrypt the message
    decrypted = decrypt_message(encrypted, key)
    print(f"Decrypted Message: {decrypted}")

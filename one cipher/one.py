import os
import logging
from setup.sprint import sprint
from setup.colors import c, r, ran, lr, lc, lg, g, ly, y
from setup.banner import banner, banner2, clear
import re

import random

def generate_key(length):
    # Generates a random key of specified length
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

def encrypt(message, key):
    encrypted_message = []
    for i in range(len(message)):
        # Convert letters to numbers (A=0, B=1, ..., Z=25)
        message_num = ord(message[i]) - ord('A')
        key_num = ord(key[i]) - ord('A')
        
        # Apply One-Time Pad encryption formula
        encrypted_num = (message_num + key_num) % 26
        encrypted_letter = chr(encrypted_num + ord('A'))
        encrypted_message.append(encrypted_letter)
        
    return ''.join(encrypted_message)

def decrypt(encrypted_message, key):
    decrypted_message = []
    for i in range(len(encrypted_message)):
        # Convert letters to numbers
        encrypted_num = ord(encrypted_message[i]) - ord('A')
        key_num = ord(key[i]) - ord('A')
        
        # Apply One-Time Pad decryption formula
        decrypted_num = (encrypted_num - key_num + 26) % 26
        decrypted_letter = chr(decrypted_num + ord('A'))
        decrypted_message.append(decrypted_letter)
        
    return ''.join(decrypted_message)

def main():
    os.system("clear")
    banner()
    message = input("Enter the message (uppercase letters only): ").upper()
    
    # Generate a random key of the same length as the message
    key = generate_key(len(message))
    print("Generated Key:", key)
    
    # Encrypt the message
    encrypted_message = encrypt(message, key)
    print("Encrypted Message:", encrypted_message)
    
    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, key)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()

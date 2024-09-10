import os
import logging
from setup.sprint import sprint
from setup.colors import c, r, ran, lr, lc, lg, g, ly, y
from setup.banner import banner, banner2, clear
# Function to encrypt text using Caesar Cipher with error handling
def encrypt(text, shift):
    try:
        result = ""
        # Traverse through each character in the text
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase letters
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            # Encrypt lowercase letters
            elif char.islower():
                result += chr((ord(char) + shift - 97) % 26 + 97)
            # Leave non-alphabetic characters unchanged
            else:
                result += char
        return result
    except Exception as e:
        print(f"An error occurred during encryption: {e}")
        return None

# Function to decrypt text using Caesar Cipher with error handling
def decrypt(text, shift):
    try:
        return encrypt(text, -shift)
    except Exception as e:
        print(f"An error occurred during decryption: {e}")
        return None

# Main function to demonstrate encryption and decryption with error handling
def main():
    os.system("clear")
    banner()
    print(" ")
    try:
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value: "))
        
        encrypted_text = encrypt(text, shift)
        if encrypted_text:
            print(f"Encrypted: {encrypted_text}")
        
            decrypted_text = decrypt(encrypted_text, shift)
            if decrypted_text:
                print(f"Decrypted: {decrypted_text}")
        else:
            print("Encryption failed.")

    except ValueError:
        print("Invalid input for shift value. Please enter an integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()

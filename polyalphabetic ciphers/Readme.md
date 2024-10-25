# Polyalphabetic Cipher (Vigenère Cipher) in Python

This project implements a Polyalphabetic Cipher (specifically the Vigenère Cipher) in Python. 
The Vigenère Cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a key.

## Features
Encryption: Encrypts a message using the Vigenère cipher algorithm.

Decryption: Decrypts a message encrypted by the Vigenère cipher.

Supports custom keys and adjusts the key length to match the message.

Handles only uppercase letters (A-Z).

## How it Works
The encryption and decryption processes work by shifting each letter in the plaintext by a number of positions defined by the key.
Each letter of the key determines how much the corresponding letter in the plaintext should be shifted.

### Key Generation
If the key is shorter than the text to be encrypted, it is repeated until its length matches the text.

#### Encryption
Each character of the plaintext is shifted by a number of positions determined by the corresponding character in the key.

#### Decryption
The reverse process of encryption is performed, where each character in the cipher text is shifted back based on the key.


Here’s a sample README.md file for your project. You can customize it further as needed:

Polyalphabetic Cipher (Vigenère Cipher) in Python
This project implements a Polyalphabetic Cipher (specifically the Vigenère Cipher) in Python. The Vigenère Cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a key.

Features
Encryption: Encrypts a message using the Vigenère cipher algorithm.
Decryption: Decrypts a message encrypted by the Vigenère cipher.
Supports custom keys and adjusts the key length to match the message.
Handles only uppercase letters (A-Z).
How it Works
The encryption and decryption processes work by shifting each letter in the plaintext by a number of positions defined by the key. Each letter of the key determines how much the corresponding letter in the plaintext should be shifted.

Key Generation
If the key is shorter than the text to be encrypted, it is repeated until its length matches the text.

Encryption
Each character of the plaintext is shifted by a number of positions determined by the corresponding character in the key.

Decryption
The reverse process of encryption is performed, where each character in the cipher text is shifted back based on the key.

### Example
def main():

    text = "HELLO"
    
    key = "KEY"
    
    key = generate_key(text, key)
    
    cipher_text = encrypt(text, key)
    
    print("Encrypted Text:", cipher_text)
    
    print("Decrypted Text:", decrypt(cipher_text, key))

if __name__ == "__main__":
    main()

# Caesar Cipher in Python

This project is an implementation of the **Caesar Cipher** in Python, featuring encryption, decryption, and error handling. The program allows users to shift letters in a text by a specified number of positions (the "shift value") to encrypt or decrypt messages.

## Features

- **Encryption**: Shifts each letter in the input text by the specified shift value.
- **Decryption**: Reverts the encrypted text back to its original form using the same shift value.
- **Error Handling**: The program includes error handling for invalid inputs, ensuring smooth execution without crashes.

## How It Works

1. The user enters a text to encrypt.
2. The user provides a shift value (an integer) that determines how many positions each letter is shifted in the alphabet.
3. The program encrypts the text and outputs the encrypted message.
4. The program then decrypts the message using the same shift value and outputs the original message.

## Code Structure

- `encrypt(text, shift)`: Encrypts the given text using the specified shift value. Handles both uppercase and lowercase letters while leaving non-alphabetic characters unchanged.
- `decrypt(text, shift)`: Decrypts the text by reversing the encryption process.
- `main()`: The entry point for the program. Handles user input and demonstrates encryption and decryption.

## Example Usage

```plaintext
Enter the text to encrypt: Hello, World!
Enter the shift value: 4
Encrypted: Lipps, Asvph!
Decrypted: Hello, World!


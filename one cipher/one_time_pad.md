# One-Time Pad Cipher in Python

This project implements a One-Time Pad (OTP) cipher in Python. 
The One-Time Pad is a highly secure encryption technique that uses a randomly generated key, or "pad," that is as long as the message to be encrypted. 
This implementation includes both encryption and decryption functions.

## Features

  - Encryption: Encrypts a message using a randomly generated key of the same length.
  - Decryption: Decrypts an encrypted message back to the original using the same key.
  - Random Key Generation: Generates a random key for each message, ensuring that every encryption is unique.

## Requirements

  - Python 3.x
  - No additional libraries are required.

### Usage

  - 1 Clone the Repository:

    git clone https://github.com/VYANKATESHNAMDAS/one-time-pad-cipher.git
    cd one-time-pad-cipher

  - 2 Run the Script:

    python otp_cipher.py

  - 3 Input: Enter your message (uppercase letters only) when prompted. The program will then:

      - Generate a random key.
        
      - Encrypt the message using the key.
      - 
      - Decrypt the message back to the original text.

## Code Structure

  - generate_key: Creates a random key that matches the length of the message.
  
  - encrypt: Encrypts the message by shifting each character based on the corresponding key character.
  
  - decrypt: Reverts the encrypted message back to the original text using the same key.
    
  - main: Coordinates input, encryption, and decryption.
   
## Example

  - plaintext

    Enter the message (uppercase letters only): HELLO
    
    Generated Key: XMCKL

    Encrypted Message: ZICVT

    Decrypted Message: HELLO

### How It Works

The OTP cipher shifts each character in the message based on the corresponding character in the key. 
Each letter is converted to a number (A=0, B=1, ..., Z=25), shifted by the key, and then converted back to a letter. The decryption process reverses this shift using the same key.

### Security Note

The One-Time Pad cipher is only secure if:

  - The key is completely random.
  - The key is as long as the message.
  - Each key is only used once and kept secret.

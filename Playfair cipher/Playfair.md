
# Playfair Cipher Implementation in Python

This project provides an implementation of the Playfair Cipher in Python. The Playfair Cipher is a manual symmetric encryption technique and was the first digraph substitution cipher. It encrypts pairs of letters (digraphs), making it harder to break compared to simpler substitution ciphers.

## Features

- Encrypts plaintext using a provided key.
- Decrypts ciphertext back to plaintext using the same key.
- Handles non-alphabetic characters by ignoring them.
- Treats the letters 'I' and 'J' as equivalent.
- Handles duplicate letters in pairs by inserting a filler letter (default: 'X').
- If the text length is odd, a filler 'X' is added at the end.

## How It Works

The Playfair cipher operates on pairs of letters:
- Letters in the same row of the 5x5 matrix are shifted to the right (or left during decryption).
- Letters in the same column are shifted down (or up during decryption).
- Otherwise, the two letters form a rectangle, and the letters at opposite corners of the rectangle are swapped.

## Key Highlights

- The cipher uses a 5x5 matrix of letters generated from a key provided by the user.
- The letter 'J' is typically excluded, and 'I' is used instead.
- Text is preprocessed to remove non-alphabet characters and handle duplicates in pairs.

## Usage

1. Clone or download the repository.
2. Run the `playfair.py` file.
3. Enter a key and the plaintext when prompted.
4. The program will output the ciphertext and the decrypted text for verification.

### Example:

```bash
Enter the key: MONARCHY
Enter the plaintext: WE ARE DISCOVERED
Ciphertext: BMODZBXDNABEKUDMUIXMMOUVIF
Decrypted text: WEAREDISCOVEREDX
```

## Code Overview

- **generate_key_matrix(key)**: Creates a 5x5 matrix from the provided key.
- **find_position(matrix, char)**: Finds the position of a character in the matrix.
- **playfair_encrypt_decrypt(text, key, mode)**: Encrypts or decrypts a given text using the Playfair cipher algorithm.
- **main()**: Handles user input and runs the encryption and decryption processes.

## Requirements

- Python 3.x

## How to Run

1. Ensure Python 3.x is installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/playfair-cipher.git
   ```
3. Navigate to the project directory:
   ```bash
   cd playfair-cipher
   ```
4. Run the script:
   ```bash
   python playfair.py
   ```

## License

This project is licensed under the MIT License.

---


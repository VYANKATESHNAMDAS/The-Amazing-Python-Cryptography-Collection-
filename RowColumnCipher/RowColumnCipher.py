import os
import logging
from setup.sprint import sprint
from setup.colors import c, r, ran, lr, lc, lg, g, ly, y
from setup.banner import banner, banner2, clear

# Configure logging
logging.basicConfig(filename='RowColumnCipher.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def encrypt(message, key):
    try:
        num_of_columns = len(key)
        num_of_rows = (len(message) + num_of_columns - 1) // num_of_columns

        padded_message = message.ljust(num_of_columns * num_of_rows)

        matrix = [padded_message[i:i + num_of_columns] for i in range(0, len(padded_message), num_of_columns)]

        ciphertext = ''.join(''.join(row[int(k) - 1] for row in matrix) for k in key)

        logging.info("Message encrypted successfully.")
        return ciphertext
    except Exception as e:
        logging.error(f"Error during encryption: {e}")
        print(f"An error occurred during encryption: {e}")

def decrypt(ciphertext, key):
    try:
        num_of_columns = len(key)
        num_of_rows = len(ciphertext) // num_of_columns

        matrix = [''] * num_of_columns
        start = 0
        for k in key:
            col_length = num_of_rows
            matrix[int(k) - 1] = ciphertext[start:start + col_length]
            start += col_length

        plaintext = ''.join(''.join(matrix[col][row] for col in range(num_of_columns)) for row in range(num_of_rows)).rstrip()

        logging.info("Message decrypted successfully.")
        return plaintext
    except Exception as e:
        logging.error(f"Error during decryption: {e}")
        print(f"An error occurred during decryption: {e}")

def main():
    try:
        os.system("clear")
        banner()
        
        print(" ")
        message = input(lg + "Enter the message: ")
        key = input(y + "Enter the key (e.g., '3214'): ")

        if not key.isdigit():
            raise ValueError("Invalid key. Key must be a string of digits.")
        
        choice = input("Select 1 for encryption or 2 for decryption: ")

        if choice == '1':
            ciphertext = encrypt(message, key)
            if ciphertext:
                print(f"Encrypted: {ciphertext}")
        elif choice == '2':
            plaintext = decrypt(message, key)
            if plaintext:
                print(f"Decrypted: {plaintext}")
        else:
            raise ValueError("Invalid choice. Please select 1 for encryption or 2 for decryption.")
    
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        print(f"Error: {ve}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

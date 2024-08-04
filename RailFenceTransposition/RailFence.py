import os
import logging
from setup.sprint import sprint
from setup.colors import c, r, ran, lr, lc, lg, g, ly, y
from setup.banner import banner, banner2, clear

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def rail_fence_encrypt(text, rails):
    """
    Encrypts the given text using the Rail Fence Cipher with the specified number of rails.

    Parameters:
        text (str): The text to be encrypted.
        rails (int): The number of rails to use in the encryption.

    Returns:
        str: The encrypted text.
    """
    if rails <= 0:
        logging.error("Number of rails must be greater than 0.")
        raise ValueError("Number of rails must be greater than 0.")
    
    rail = [['' for _ in range(len(text))] for _ in range(rails)]
    direction_down = None
    row, col = 0, 0

    for char in text:
        rail[row][col] = char
        col += 1

        if row == 0 or row == rails - 1:
            direction_down = not direction_down

        row += 1 if direction_down else -1

    encrypted_text = ''.join([''.join(rail[i]) for i in range(rails)])
    logging.info("Text encrypted successfully.")
    return encrypted_text


def rail_fence_decrypt(encrypted_text, rails):
    """
    Decrypts the given encrypted text using the Rail Fence Cipher with the specified number of rails.

    Parameters:
        encrypted_text (str): The text to be decrypted.
        rails (int): The number of rails used in the encryption.

    Returns:
        str: The decrypted text.
    """
    if rails <= 0:
        logging.error("Number of rails must be greater than 0.")
        raise ValueError("Number of rails must be greater than 0.")
    
    rail = [['' for _ in range(len(encrypted_text))] for _ in range(rails)]
    direction_down = None
    row, col = 0, 0

    for char in encrypted_text:
        rail[row][col] = '*'
        col += 1

        if row == 0 or row == rails - 1:
            direction_down = not direction_down

        row += 1 if direction_down else -1

    index = 0
    for i in range(rails):
        for j in range(len(encrypted_text)):
            if rail[i][j] == '*':
                rail[i][j] = encrypted_text[index]
                index += 1

    decrypted_text = []
    row, col = 0, 0
    for _ in range(len(encrypted_text)):
        decrypted_text.append(rail[row][col])
        col += 1

        if row == 0 or row == rails - 1:
            direction_down = not direction_down

        row += 1 if direction_down else -1

    logging.info("Text decrypted successfully.")
    return ''.join(decrypted_text)


def main():
    os.system("clear")
    banner()
    print(" ")
    """
    Main function to execute the Rail Fence Cipher encryption and decryption based on user choice.
    """
    try:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").strip().upper()
        
        if choice not in ('E', 'D'):
            logging.error("Invalid choice. Please select 'E' to encrypt or 'D' to decrypt.")
            return

        text = input("Enter the text: ")
        rails = int(input("Enter the number of rails: "))

        if choice == 'E':
            # Encrypt the text
            encrypted = rail_fence_encrypt(text, rails)
            print(f"Encrypted: {encrypted}")

        elif choice == 'D':
            # Decrypt the text
            decrypted = rail_fence_decrypt(text, rails)
            print(f"Decrypted: {decrypted}")

    except ValueError as e:
        logging.error(f"ValueError: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

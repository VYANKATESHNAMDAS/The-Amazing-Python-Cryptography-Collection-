import os
from setup.sprint import sprint
from setup.colors import c, r, ran, lr, lc, lg, g, ly, y
from setup.banner import banner, banner2, clear
def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(text, key):
    cipher_text = []
    for i in range(len(text)):
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)

def decrypt(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)

def main():
    os.system("clear")
    banner()
    print(" ")
    text =input("Enter any tact that you want to be Encrypted/Decreapted =") 
    key = input("Enter a KEY = ")
    key = generate_key(text, key)
    cipher_text = encrypt(text, key)
    print("Encrypted Text:", cipher_text)
    print("Decrypted Text:", decrypt(cipher_text, key))

if __name__ == "__main__":
    main()

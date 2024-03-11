from my_module.functions import encrypt_text, decrypt_text, brute_force
from my_module.classes import CaesarCipher


def main():
    print("Make your message a secret! (Caesar Cipher Edition)")

    cipher = CaesarCipher()

    while True:
        option = input("Would you like to encrypt or decrypt a message?\n(0: encrypt, 1: decrypt, 2: HACK-brute force): ")
        if option == '0':   # encrypt
            message = input("Enter your message: ")
            shift = input("Enter the shift amount: ")
            encr_message = encrypt_text(cipher, message, int(shift))
            
            print(f"Original Message: {message}")
            print(f"Encrypted Message: {encr_message}")

        elif option == '1':     #decrypt
            encr_message = input("Enter Encrypted Message: ")
            shift = input("Enter the magic code: ")
            
            decr_message = decrypt_text(cipher, encr_message, int(shift))
        
            print(f"Encrypted Message: {encr_message}")
            print(f"Decrypted! Original Message: {decr_message}")

        elif option == '2': #brute force
            encr_message = input("Enter Encrypted Message: ")
            brute_force(cipher, encr_message)
        

        else:
            print("Invalid Entry. Please Type 0 or 1 or 2 with no spaces.")
            continue

        break

if __name__ == "__main__":
    main()
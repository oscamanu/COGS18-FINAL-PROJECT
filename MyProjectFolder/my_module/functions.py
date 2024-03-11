def encrypt_text(cipher, text, shift):
    return cipher.encrypt(text, shift)

def decrypt_text(cipher, text, shift):
    return cipher.decrypt(text, shift)

def brute_force(cipher, encr_message):
    return cipher.bruteforce(encr_message)
#class Dog():
#    sound = 'Woof'
#    def __init__(self, name):
#        self.name = name
#   def speak(self, n_times=2):
#        return self.sound * n_times

class CaesarCipher:
    def __init__(self):
        # store the alpha and digits (digits arent required but i will shift them anyways)
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    def encrypt_letter(self, letter, shift):
        i = 0

        if letter in self.alphabet:
            for alpha in self.alphabet:
                if letter == alpha:
                    return self.alphabet[(i + shift) % 26]
                i = i + 1
        
        elif letter in self.number:
            for num in self.number:
                if letter == num:
                    return self.number[(i + shift) % 10]
                i = i + 1
        
        else:
            return letter

    def encrypt(self, message, shift):
        message = message.upper()
        encrypted_message = ""
        
        for letter in message:
            encrypted_message += self.encrypt_letter(letter, shift)
        
        return encrypted_message
 
    def decrypt_letter(self, letter, shift):
        return self.encrypt_letter(letter, -shift)

    def decrypt(self, encrypted_message, shift):
        encrypted_message = encrypted_message.upper()
        decrypted_message = ""
        for letter in encrypted_message:
            decrypted_message += self.decrypt_letter(letter, shift)
        return decrypted_message

    def bruteforce(self, encr_message):
        print("All Possible Decryptions of: ", encr_message)
        for i in range(26):
            message = self.decrypt(encr_message, i)
            print(f"{i} ) {message}" if i >= 10 else f"{i} )  {message}")

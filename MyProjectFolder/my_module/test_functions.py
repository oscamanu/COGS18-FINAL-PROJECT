from classes import CaesarCipher
from functions import encrypt_text, decrypt_text, brute_force 

cipher = CaesarCipher()


def test_encr():
    message = "HELLO"
    shift = 5
    assert encrypt_text(cipher, message, shift) == "MJQQT"

    message = "APPLE"
    shift = 1
    assert encrypt_text(cipher, message, shift) == "BQQMF"

    message = "COGS FINAL PROJECT"
    shift = 21
    assert encrypt_text(cipher, message, shift) == "XJBN ADIVG KMJEZXO"



def test_decr():
    message = "MJQQT"
    shift = 5
    assert decrypt_text(cipher, message, shift) == "HELLO"

    message = "BQQMF"
    shift = 1
    assert decrypt_text(cipher, message, shift) == "APPLE"

    message = "XJBN ADIVG KMJEZXO"
    shift = 21
    assert decrypt_text(cipher, message, shift) == "COGS FINAL PROJECT"

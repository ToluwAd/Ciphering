"""
This program is used to decrypt a ciphered code
Author: Adejumo Toluwani
When: February 7, 2023
"""

UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_CASE = "abcdefghijklmnopqrstuvwxyz"


def decrypt_caesar(text: str, shift: int):
    """
    This function decrypts a ciphered text by moving the letter in the alphabet a specified number of times to the left.
    """

    decrypted_text = ""
    for char in text:

        # This block of code decrypts uppercase letters in the users input

        if char in UPPER_CASE:
            letter_in_alphabet = UPPER_CASE.find(char)  # finds the position of the letters in the user's input in
            # global constant, "UPPER_CASE"
            new_letter = (letter_in_alphabet - shift) % 26  # Gets the new ciphered letter
            decrypted_text += UPPER_CASE[new_letter]

            # This block of code decrypts lowercase letters in the user's input

        elif char in LOWER_CASE:
            letter_in_alphabet = LOWER_CASE.find(char)  # finds the position of the letters in the user's input in
            # global constant, "LOWER_CASE"
            new_letter = (letter_in_alphabet - shift) % 26  # Gets the new ciphered letter
            decrypted_text += LOWER_CASE[new_letter]
        else:
            decrypted_text += char

    return decrypted_text


def main():
    """
    This function prints out the decrypted text in caesar cipher
    """
    text = input("Enter a text to decipher: ")
    deciphered_text = decrypt_caesar(text, 3)
    print(deciphered_text)


main()

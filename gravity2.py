"""
This program is used to decrypt a ciphered code using two different methods
Author: Adejumo Toluwani
When: February 8th, 2023
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
    pass


def decrypt_atbash(text: str):
    """
    This function decrypts a ciphered text by reversing its position in the alphabet
    """

    atbash_text = ""

    for char in text:

        # This block of code deals with the uppercase letters in the user's input

        if char in UPPER_CASE:
            letter = UPPER_CASE.find(char)  # finds the position of the letters in the user's input in global
            # constant, "UPPER_CASE"
            new_letter = abs(letter - 25)  # Gets the new ciphered letter
            atbash_text += UPPER_CASE[new_letter]

        # This block of code deals with the lowercase letters in the user's input

        elif char in LOWER_CASE:
            letter = LOWER_CASE.find(char)  # finds the position of the letters in the user's input in global
            # constant, "LOWER_CASE"
            new_letter = abs(letter - 25)  # Gets the new ciphered letter
            atbash_text += LOWER_CASE[new_letter]

        else:
            atbash_text += char

    return atbash_text


def main():
    """
    This function prints out the text ciphered in both caesar and atbash.
    """
    text = input("Enter a text to decipher: ")
    caesar_text = decrypt_caesar(text, 3)
    atbash_text = decrypt_atbash(text)
    print("Let's try all the methods we have:")
    print(f"Caesar cipher:  {caesar_text} \nAtbash cipher:  {atbash_text}")


main()

"""
This program is used to decrypt a ciphered code using three different methods
Author: Adejumo Toluwani
When: February 8th, 2023
"""

UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_CASE = "abcdefghijklmnopqrstuvwxyz"
Numbers = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26"


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


def decrypt_atbash(text: str):
    """
    This function decrypts a ciphered text by reversing the alphabet
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


def decrypt_a1z26(text):
    """
    This function takes a number and returns its alphabetical counterpart
    """
    a1z26_text = ""

    # This block of code splits the input into numeric and non-numeric parts

    list_of_all_characters = []
    character = ""
    for char in text:
        if char.isdigit():
            character += char
        else:
            list_of_all_characters.append(character)
            character = ""
            list_of_all_characters.append(char)  # Gets all the characters in text and puts it in a list
    if character:
        list_of_all_characters.append(character)

    # This block of code loops through each element and convert numbers to letters

    for element in list_of_all_characters:
        if element.isdigit() and element in Numbers:
            letter = chr(int(element) + 64)  # Gets the alphabetical counterpart by subtracting one less than the
            # ordinal value for A
            a1z26_text += letter
        else:
            a1z26_text += element
            a1z26_text = a1z26_text.replace("-", "")
    return a1z26_text


def main():
    """
    This function prints out a ciphered text in caesar, atbash and a1z26
    """
    text = input("Enter a text to decipher: ")
    caesar_text = decrypt_caesar(text, 3)
    atbash_text = decrypt_atbash(text)
    a1z26_text = decrypt_a1z26(text)
    print("Let's try all the methods we have")
    print("Caesar cipher: ", caesar_text, "\nAtbash cipher: ", atbash_text, "\nA1Z26 cipher: ", a1z26_text)


main()

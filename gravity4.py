"""
This program is used to decrypt a ciphered code using two different methods
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
            new_letter = (letter_in_alphabet - shift) % 26
            decrypted_text += UPPER_CASE[new_letter]

            # This block of code decrypts lowercase letters in the user's input

        elif char in LOWER_CASE:
            letter_in_alphabet = LOWER_CASE.find(char)  # finds the position of the letters in the user's input in
            # global constant, "LOWER_CASE"
            new_letter = (letter_in_alphabet - shift) % 26
            decrypted_text += LOWER_CASE[new_letter]
        else:
            decrypted_text += char

    return decrypted_text


def decrypt_atbash(text):
    """
    This function decrypts a ciphered text by reversing the alphabet
    """

    atbash_text = ""

    for char in text:

        # This block of code deals with the uppercase letters in the user's input

        if char in UPPER_CASE:
            letter = UPPER_CASE.find(char)  # finds the position of the letters in the user's input in global
            # constant, "UPPER_CASE"
            new_letter = abs(letter - 25)
            atbash_text += UPPER_CASE[new_letter]

        # This block of code deals with the lowercase letters in the user's input

        elif char in LOWER_CASE:
            letter = LOWER_CASE.find(char)  # finds the position of the letters in the user's input in global
            # constant, "LOWER_CASE"
            new_letter = abs(letter - 25)
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
    current_part = ""
    for char in text:
        if char.isdigit():
            current_part += char
        else:
            list_of_all_characters.append(current_part)
            current_part = ""
            list_of_all_characters.append(char)  # Gets all the characters in text and puts it in a list

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


def decrypt_caesar_then_atbash(text):
    """
    This function decrypts a text in caesar and then atbash
    """
    caesar_translation = decrypt_caesar(text, 3)
    combination_of_caesar_and_atbash = decrypt_atbash(caesar_translation)
    return combination_of_caesar_and_atbash


def decrypt_atbash_then_caesar(text):
    """
    This function decrypts a text in atbash and then caesar
    """
    atbash_translation = decrypt_atbash(text)
    combination_of_atbash_and_caesar = decrypt_caesar(atbash_translation, 3)
    return combination_of_atbash_and_caesar


def decrypt_a1z26_then_caesar(text):
    """
    This function decrypts a text in a1z26 and then caesar
    """
    a1z26_translation = decrypt_a1z26(text)
    combination_of_a1z26_and_caesar = decrypt_caesar(a1z26_translation, 3)
    return combination_of_a1z26_and_caesar


def decrypt_a1z26_then_atbash(text):
    """
    This function decrypts a text in a1z26 and then atbash
    """
    a1z26_translation = decrypt_a1z26(text)
    combination_of_a1z26_and_atbash = decrypt_atbash(a1z26_translation)
    return combination_of_a1z26_and_atbash


def decrypt_a1z26_then_atbash_then_caesar(text):
    """
    This function decrypts a text in a1z26 then atbash and then caesar
    """
    a1z26_translation = decrypt_a1z26(text)
    combination_of_a1z26_and_atbash = decrypt_atbash(a1z26_translation)
    combination_of_a1z26_and_atbash_and_caesar = decrypt_caesar(combination_of_a1z26_and_atbash, 3)
    return combination_of_a1z26_and_atbash_and_caesar


def decrypt_a1z26_then_caesar_then_atbash(text):
    a1z26_translation = decrypt_a1z26(text)
    combination_of_a1z26_and_caesar = decrypt_caesar(a1z26_translation, 3)
    combination_of_a1z26_and_caesar_and_atbash = decrypt_atbash(combination_of_a1z26_and_caesar)
    return combination_of_a1z26_and_caesar_and_atbash


def main():
    """
    This function prints out multiple variations of a ciphered code
    """
    text = input("Enter a text to decipher: ")
    caesar_text = decrypt_caesar(text, 3)
    atbash_text = decrypt_atbash(text)
    caesar_and_atbash = decrypt_caesar_then_atbash(text)
    atbash_and_caesar = decrypt_atbash_then_caesar(text)
    a1z26_text = decrypt_a1z26(text)
    a1z26_and_caesar = decrypt_a1z26_then_caesar(text)
    a1z26_and_atbash = decrypt_a1z26_then_atbash(text)
    a1z26_and_atbash_and_caesar = decrypt_a1z26_then_atbash_then_caesar(text)
    a1z26_and_caesar_and_atbash = decrypt_a1z26_then_caesar_then_atbash(text)

    print("Let's try all the methods we have:")
    print(f"Caesar cipher:  {caesar_text} \nAtbash cipher:  {atbash_text} \nCombined: 1) Caesar; 2) Atbash cipher: "
          f"{caesar_and_atbash} \nCombined: 1) Atbash; 2) Caesar cipher: {atbash_and_caesar} \nA1Z26 cipher: "
          f"{a1z26_text} \nCombined: 1) A1Z26; 2) Caesar cipher: {a1z26_and_caesar} \nCombined: 1) A1Z26; 2) "
          f"Atbash cipher: {a1z26_and_atbash} \nCombined: 1) A1Z26; 2) Atbash; 3) Caesar cipher: "
          f"{a1z26_and_atbash_and_caesar} \nCombined: 1) A1Z26; 2) Caesar; 3) Atbash cipher: "
          f"{a1z26_and_caesar_and_atbash}")


main()

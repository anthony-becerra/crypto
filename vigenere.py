from helpers import alphabet_position, rotate_character
from sys import argv, exit

def encrypt(user_text, user_key):
    # Create variables
    encrypted_message = ''
    key_index = 0

    # Change user_key into list of ordinal values
    ord_user_key = []
    for char in user_key:
        char = char.lower()
        char_rotate = chr(ord(char) - ord('a'))
        ord_user_key.append(ord(char_rotate))

    # Loop through user_text
    for char in user_text:
        # Counter to loop through key index - modulo in range of key length
        key_index = key_index % (len(user_key))
        if char.isalpha() == True:
            encrypted_message += rotate_character(char, ord_user_key[key_index])
            key_index += 1
        else:
            encrypted_message += rotate_character(char, ord_user_key[key_index])

    return encrypted_message

def main():
    #Validate argv is only alphabetic characters
    for char in argv[1]:
        if char.isalpha() == False:
            print('''usage: python vigenere.py keyword
Arguments:
-keyword : The string to be used as a "key" to encrypt your message. Should only contain alphabetic characters-- no numbers or special characters.''')
            exit()
    #Validate number of arguments passed into program
    if len(argv) != 2:
        print('''usage: python vigenere.py keyword
Arguments:
-keyword : The string to be used as a "key" to encrypt your message. Should only contain alphabetic characters-- no numbers or special characters.''')
        exit()

    else:
        user_text = input("Enter the message you want to encrypt: ")
        #user_key = input("Enter your secret cipher key: ")
        print(encrypt(user_text, argv[1]))

if __name__ == "__main__":
    main()

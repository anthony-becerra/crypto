from helpers import alphabet_position, rotate_character
from sys import argv, exit

def encrypt(text, rot):
    encrypted_message = ''
    for i in text:
        encrypted_message += rotate_character(i, rot)
    return encrypted_message

def main():
    if len(argv) != 2:
        print("usage: python caesar.py n >>> where n is an integer")
        exit()
    elif argv[1].isdigit() == False:
        print("usage: python caesar.py n >>> where n is an integer")
        exit()
    else:
        user_text_input = input("Type a message: ")
        #user_rotation_input = int(input("Rotate by: "))
        print(encrypt(user_text_input, int(argv[1])))

if __name__ == '__main__':
    main()

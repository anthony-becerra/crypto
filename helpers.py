def alphabet_position(letter):
    alphabet_num = ord(letter)
    if alphabet_num >= 97:
        alphabet_num -= 97
    else:
        alphabet_num -= 65
    return alphabet_num

def rotate_character(char, rot):
    char_rotate = ''
    if char.isalpha() == True:
        if char >= 'A' and char <= 'Z':
            char_rotate = chr((alphabet_position(char) + rot) % 26 + ord('A'))
        elif char >= 'a' and char <= 'z':
            char_rotate = chr((alphabet_position(char) + rot) % 26 + ord('a'))
    else:
        char_rotate = char #changed += to =
    return char_rotate

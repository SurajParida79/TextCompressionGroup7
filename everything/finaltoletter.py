def read_Text(file_path):
    my_file = open(file_path, "r", encoding='utf-8')
    string = my_file.read()
    return string


def findletter(my_char):
    if my_char == '1100':
        code = 'a'
    elif my_char == '1100010':
        code = 'b'
    elif my_char == '1100100':
        code = 'c'
    elif my_char == '1101000':
        code = 'd'
    elif my_char == '1111':
        code = 'e'
    elif my_char == '1110001':
        code = 'f'
    elif my_char == '1110010':
        code = 'g'
    elif my_char == '1010':
        code = 'h'
    elif my_char == '0000':
        code = 'i'
    elif my_char == '1111001':
        code = 'j'
    elif my_char == '1111010':
        code = 'k'
    elif my_char == '1001':
        code = 'l'
    elif my_char == '1111101':
        code = 'm'
    elif my_char == '1111110':
        code = 'n'
    elif my_char == '1000':
        code = 'o'
    elif my_char == '1111':
        code = 'p'
    elif my_char == '1110001':
        code = 'q'
    elif my_char == '1011':
        code = 'r'
    elif my_char == '1101':
        code = 's'
    elif my_char == '1110':
        code = 't'
    elif my_char == '1110101':
        code = 'u'
    elif my_char == '1110110':
        code = 'v'
    elif my_char == '1110111':
        code = 'w'
    elif my_char == '1111000':
        code = 'x'
    elif my_char == '1111001':
        code = 'y'
    elif my_char == '1111010':
        code = 'z'
    elif my_char == '1000001':
        code = 'A'
    elif my_char == '1000010':
        code = 'B'
    elif my_char == '1000011':
        code = 'C'
    elif my_char == '1000100':
        code = 'D'
    elif my_char == '1000101':
        code = 'E'
    elif my_char == '1000110':
        code = 'F'
    elif my_char == '1000111':
        code = 'G'
    elif my_char == '1001000':
        code = 'H'
    elif my_char == '1001001':
        code = 'I'
    elif my_char == '1001010':
        code = 'J'
    elif my_char == '1001100':
        code = 'K'
    elif my_char == '1001101':
        code = 'L'
    elif my_char == '1001110':
        code = 'M'
    elif my_char == '1001111':
        code = 'N'
    elif my_char == '1010000':
        code = 'O'
    elif my_char == '1010001':
        code = 'P'
    elif my_char == '1010010':
        code = 'Q'
    elif my_char == '1010100':
        code = 'R'
    elif my_char == '1011000':
        code = 'S'
    elif my_char == '1011001':
        code = 'T'
    elif my_char == '1011010':
        code = 'U'
    elif my_char == '1011100':
        code = 'V'
    elif my_char == '1011101':
        code = 'W'
    elif my_char == '1011110':
        code = 'X'
    elif my_char == '1011111':
        code = 'Y'
    elif my_char == '1100000':
        code = 'Z'
    elif my_char == '0100000':
        code = ' '
    elif my_char == '0101110':
        code = '.'
    elif my_char == '0101100':
        code = ','
    elif my_char == '0101101':
        code = '-'
    elif my_char == "0100111":
        code = "'"
    elif my_char == "0000011":
        code = '\n'
    elif my_char == '0100010':
        code = '"'
    elif my_char == "0100001":
        code = '!'
    return code


def toletter(string):
    myletter = ""
    string = read_Text("BinOutput.txt")
    for i in range(0, len(string)):
        code2 = findletter(string[i])
        myletter = myletter + code2
    return myletter

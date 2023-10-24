import os


def write_string_to_file(directory_path, file_name, initial_content):
    try:
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, 'w') as file:
            file.write(initial_content)
            print("done")
    except Exception as e:
        print(f"Error: {str(e)}")


def findletter(my_char):
    if my_char == '1100':
        code = 'a'
    elif my_char == '1100010':
        code = 'b'
    elif my_char == '1100100':
        code = 'c'
    elif my_char == '1101000':
        code = 'd'
    elif my_char == '0111':
        code = 'e'
    elif my_char == '01100110':
        code = 'f'
    elif my_char == '1110010':
        code = 'g'
    elif my_char == '1010':
        code = 'h'
    elif my_char == '0000':
        code = 'i'
    elif my_char == '1101010':
        code = 'j'
    elif my_char == '01101011':
        code = 'k'
    elif my_char == '10011':
        code = 'l'
    elif my_char == '1111101':
        code = 'm'
    elif my_char == '1111110':
        code = 'n'
    elif my_char == '10001':
        code = 'o'
    elif my_char == '1111':
        code = 'p'
    elif my_char == '01110001':
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
    elif my_char == '01111010':
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
    elif my_char == '0':
        code = '0'
    elif my_char == '1':
        code = '1'
    elif my_char == '10':
        code = '2'
    elif my_char == '11':
        code = '3'
    elif my_char == '100':
        code = '4'
    elif my_char == '101':
        code = '5'
    elif my_char == '110':
        code = '6'
    elif my_char == '111':
        code = '7'
    elif my_char == '1000':
        code = '8'
    elif my_char == '1001':
        code = '9'
    else:
        code = 'error'
    return code


def toletter(string):
    listtostring = string.split(" ")
    myletter = ""
    for binary in listtostring:
        code1 = findletter(binary)
        myletter = myletter + code1
    return myletter

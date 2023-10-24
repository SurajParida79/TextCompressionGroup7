import os
def findbinary(my_char):
    if my_char == 'a':
        code = '1100'
    elif my_char == 'b':
        code = '1100010'
    elif my_char == 'c':
        code = '1100100'
    elif my_char == 'd':
        code = '1101000'
    elif my_char == 'e':
        code = '0111'
    elif my_char == 'f':
        code = '01100110'
    elif my_char == 'g':
        code = '1110010'
    elif my_char == 'h':
        code = '1010'
    elif my_char == 'i':
        code = '0000'
    elif my_char == 'j':
        code = '1101010'
    elif my_char == 'k':
        code = '01101011'
    elif my_char == 'l':
        code = '10011'
    elif my_char == 'm':
        code = '1111101'
    elif my_char == 'n':
        code = '1111110'
    elif my_char == 'o':
        code = '10001'
    elif my_char == 'p':
        code = '1111'
    elif my_char == 'q':
        code = '01110001'
    elif my_char == 'r':
        code = '1011'
    elif my_char == 's':
        code = '1101'
    elif my_char == 't':
        code = '1110'
    elif my_char == 'u':
        code = '1110101'
    elif my_char == 'v':
        code = '1110110'
    elif my_char == 'w':
        code = '1110111'
    elif my_char == 'x':
        code = '1111000'
    elif my_char == 'y':
        code = '1111001'
    elif my_char == 'z':
        code = '01111010'
    elif my_char == 'A':
        code = '1000001'
    elif my_char == 'B':
        code = '1000010'
    elif my_char == 'C':
        code = '1000011'
    elif my_char == 'D':
        code = '1000100'
    elif my_char == 'E':
        code = '1000101'
    elif my_char == 'F':
        code = '1000110'
    elif my_char == 'G':
        code = '1000111'
    elif my_char == 'H':
        code = '1001000'
    elif my_char == 'I':
        code = '1001001'
    elif my_char == 'J':
        code = '01101010'
    elif my_char == 'K':
        code = '1001100'
    elif my_char == 'L':
        code = '1001101'
    elif my_char == 'M':
        code = '1001110'
    elif my_char == 'N':
        code = '1001111'
    elif my_char == 'O':
        code = '1010000'
    elif my_char == 'P':
        code = '1010001'
    elif my_char == 'Q':
        code = '1010010'
    elif my_char == 'R':
        code = '1010100'
    elif my_char == 'S':
        code = '1011000'
    elif my_char == 'T':
        code = '1011001'
    elif my_char == 'U':
        code = '1011010'
    elif my_char == 'V':
        code = '1011100'
    elif my_char == 'W':
        code = '1011101'
    elif my_char == 'X':
        code = '1011110'
    elif my_char == 'Y':
        code = '01111001'
    elif my_char == 'Z':
        code = '1100000'
    elif my_char == ' ':
        code = '0100000'
    elif my_char == '.':
        code = '0101110'
    elif my_char == ',':
        code = '0101100'
    elif my_char == '-':
        code = '0101101'
    elif my_char == "'":
        code = '0100111'
    elif my_char == "\n":
        code = '0000011'
    elif my_char == '"':
        code = '0100010'
    elif my_char == "!":
        code = '0100001'
    elif my_char == '0':
        code = '0'
    elif my_char == '1':
        code = '1'
    elif my_char == '2':
        code = '10'
    elif my_char == '3':
        code = '11'
    elif my_char == '4':
        code = '100'
    elif my_char == '5':
        code = '101'
    elif my_char == '6':
        code = '110'
    elif my_char == '7':
        code = '111'
    elif my_char == '8':
        code = '1000'
    elif my_char == '9':
        code = '1001'
    else:
        code = 'error'
    return code


def tobinary(string):
    mybinary = ""
    for i in range(0, len(string)):
        code1 = findbinary(string[i])
        code2 = code1 + " "
        mybinary = mybinary + code2
    return mybinary


def write_string_to_file(directory_path, file_name, initial_content):
    try:
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, 'w') as file:
            file.write(initial_content)
            print("done")
    except Exception as e:
        print(f"Error: {str(e)}")



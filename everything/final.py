import finaltobinary
import finaltoletter
import difflib
import os


# 1 Read file of text and convert to binary
# + save file

def readwords(file):
    my_file = open(file, "r", encoding='utf-8')
    string = my_file.read()
    string2 = finaltobinary.tobinary(string)
    finaltobinary.write_string_to_file('/Users/kenny/PycharmProjects/ECSproject/venv', "BinOutput.txt", string2)
    print(string2)

# 2 Read file of binary and convert to words

def readbinary():
    my_file = open("BinOutput.txt", "r", encoding= 'utf-8')
    string3 = my_file.read()
    string4 = finaltoletter.toletter(string3)
    return string4

# 3 Compare the two files

def compare(binary_file_path, text_file_path):
    with open(binary_file_path, 'rb') as binary_file:
        binary_data = binary_file.read()
    with open(text_file_path, 'r', encoding = 'utf-8') as text_file:
        text_data = text_file.read()
    similarity_ratio = difflib.SequenceMatcher(None, binary_data, text_data).ratio()

    return similarity_ratio



import finaltobinary
import finaltoletter
import difflib
import os

def readwords(file):
    my_file = open(file, "r", encoding='utf-8')
    string = my_file.read()
    string2 = finaltobinary.tobinary(string)
    finaltobinary.write_string_to_file('', "BinOutput.txt", string2)
    return(string2)

if __name__ == "__main__":
    readwords("Words.txt")
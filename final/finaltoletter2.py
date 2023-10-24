import finaltobinary
import finaltoletter
import difflib
import os

def readbinary(file):
    my_file = open(file, "r", encoding='utf-8')
    string = my_file.read()
    string2 = finaltoletter.toletter(string)
    finaltoletter.write_string_to_file('', "StrOutput.txt", string2)
    return(string2)

if __name__ == "__main__":
    readbinary("BinOutput.txt")
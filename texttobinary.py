import binaryconverstion

def read_Text(file_path):
    my_file = open(file_path, "r", encoding='utf-8')
    string = my_file.read()
    return string

    string = read_Text(file_path)
    ans = binaryconverstion.letters(string)
    compress_file = open("H:/BinOutput.txt", "w")
    compress_file.write(len(ans) + "." + ans)
    compress_file.close()
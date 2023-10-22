import binaryconversion


def text_to_string(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        file_contents = file.read()
    return file_contents


def binary_to_text(binary_data):
    text_data = binary_data.decode("utf-8")
    return text_data


file_contents = text_to_string("BinOutput.txt")
binary_data = binaryconversion.letters(file_contents)
binary_to_text(binary_data)

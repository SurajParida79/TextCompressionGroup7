def binary_to_text_one(input_binary_file):
    with open(input_binary_file, "rb") as binary_file:
        binary_data = binary_file.read()
        global text_data
        text_data = binary_data.decode("utf-8")


def binary_to_text_two(output_text_file):
    with open(output_text_file, "w") as text_file:
        text_file.write(text_data)


if __name__ == "__main__:":
    input_binary_file = "binary_data.bin"
    output_text_file = "BinOutput.txt"
    binary_to_text_one(input_binary_file)
    binary_to_text_two(output_text_file)

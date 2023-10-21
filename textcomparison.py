import difflib


def compare(binary_file_path, text_file_path):
    with open(binary_file_path, 'rb') as binary_file:
        binary_data = binary_file.read()
    with open(text_file_path, 'r', encoding = 'utf-8') as text_file:
        text_data = text_file.read()
    similarity_ratio = difflib.SequenceMatcher(None, binary_data, text_data).ratio()

    return similarity_ratio
def get_num_words(document):
    num_words = 0
    document = document.split()
    for word in document:
        num_words += 1

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")


def get_num_letters(document):
    dict_of_chars = {}
    document = document.lower()

    for char in document:
        if char not in dict_of_chars:
            dict_of_chars[char] = 1
        else:
            dict_of_chars[char] += 1

    return dict_of_chars


def sort_on(items):
    return items["num"]


def dict_into_list(dict_of_chars):
    chars_list = []

    for key, value in dict_of_chars.items():
        chars_list.append({"char": key, "num": value})

    return chars_list

from operator import le


frankenstein_book = "books/frankenstein.txt"


def open_file(file):
    """Generates a string from a text file

    Returns:
        String of the text file.
    """
    with open(file) as f:
        file_contents = f.read()
        return file_contents


def count_book_words(file):
    """Shows in console how many words does the file text content"""
    book = open_file(file)
    words = book.split()
    print(f"The document has {len(words)} words")


def count_characters(file):
    """Shows in console how many characters the file has
    and how many times they're repeated
    """
    characters = "abcdefghijklmnopqrstuvwxyz"
    num_char_dict = {}
    # Create a dictionary with all the characters
    for char in characters:
        num_char_dict[char] = 0
    # Lower the text
    text = open_file(file)
    lowered_text = text.lower()
    # Increment the number of times a character appears
    for letter in lowered_text:
        if letter in characters:
            num_char_dict[letter] += 1

    print(
        f"The number of times that different characters appear in the document\n{num_char_dict}"
    )


def main():
    count_book_words(frankenstein_book)
    count_characters(frankenstein_book)


main()

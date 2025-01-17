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


def main():
    count_book_words(frankenstein_book)


main()

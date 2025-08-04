import sys
from stats import get_num_words, get_num_letters, sort_on, dict_into_list


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    # Get word count
    get_num_words(book_text)
    
    # Get character count
    letters = get_num_letters(book_text)
    letters_list = dict_into_list(letters)
    letters_list.sort(reverse=True, key=sort_on)
    
    # Print character count report
    print("--------- Character Count -------")
    for item in letters_list:
        # Only print alphabetical characters
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")


main()

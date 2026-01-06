import sys
from stats import count_words, count_letters, sort_by_number

def get_book_text(_path_to_file):
    with open(_path_to_file) as f:
        content_ = f.read()
    return content_
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(sys.argv)
    #return
    path_to_book = sys.argv[1]
    text = get_book_text(path_to_book)
    number_of_words = count_words(text)
    char_dict = count_letters(text)
    char_dict_sorted = sort_by_number(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for entry_ in char_dict_sorted:
        if not entry_['char'].isalpha():
            continue
        print(f"{entry_['char']}: {entry_['num']}")
    print("============= END ===============")
main()
from stats import get_num_words, character_count, chars_dict_to_sorted_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    chars = character_count(text)
    sorted_list = chars_dict_to_sorted_list(chars)
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print("============= END ===============")

main()
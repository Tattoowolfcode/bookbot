def get_num_words(book_contents):
    words = book_contents.split()
    num_words = len(words)
    return num_words

def character_count(book_contents):
    lowercase = book_contents.lower()
    char_count = {}
    for c in lowercase:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

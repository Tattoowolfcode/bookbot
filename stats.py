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

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(char_counts):
    sorted_list = []
    for ch in char_counts:
        sorted_list.append({"char": ch, "num": char_counts[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_char(book_text):
    lower_char = book_text.lower()
    char_dict = {}
    for char in lower_char:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_chars(char_count):
    chars_list = []
    for char, count in char_count.items():
        chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse=True, key=lambda d: d["count"])
    return chars_list


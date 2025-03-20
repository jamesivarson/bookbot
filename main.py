def get_book_text(book_path):
    with open(book_path, "r", encoding="utf-8") as f:
              file_contents = f.read()
              return file_contents
def main():
    import stats
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    word_count = 0
    book_text = None
    char_count = {}
    char_list = []
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = stats.count_words(book_text)
    char_count = stats.count_char(book_text)
    char_list = stats.sort_chars(char_count)
    char_list.sort(reverse=True, key=lambda d: d["count"])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in char_list:
          if i["char"].isalpha():
              print(f"{i['char']}: {i['count']}")
    print("============= END ===============")
main()
from stats import count_words
from stats import words_counter 
from stats import sort_on

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    counter = count_words(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {counter} total words")
    print("--------- Character Count -------")
    char_counts = words_counter(text)
    char_counts.sort(reverse=True, key=sort_on)
    for item in char_counts:
        print(f"{item['char']}: {item['num']}")
    print("========== END ==========")


main()

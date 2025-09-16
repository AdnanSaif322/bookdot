from stats import count_words
from stats import words_counter 

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    counter = count_words(text)
    print(f"{counter} words found in the document")
    char_counts = words_counter(text)
    print(f"{char_counts}")


main()

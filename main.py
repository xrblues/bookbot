import re

def main():
    file_contents = read_book("books/frankenstein.txt")
    words = count_words(file_contents)
    gen_letter_report(file_contents)
    # count_chars(file_contents)

def read_book(book_path):
    print(f"--- Begin report of {book_path}---")
    with open(book_path) as f:
        file_contents = f.read()
        # print(file_contents)
        return file_contents

def count_words(book_string):
    words = len(book_string.split())
    print(f"{words} found in the document")
    return words

def count_chars(book_string):
    char_count = {}
    for char in book_string:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    print(char_count)
    return char_count

def gen_letter_report(book_string):
    alpha_count = {}
    for char in book_string:
        char = char.lower()
        if char.isalpha():  # Check if char is a letter
            alpha_count[char] = alpha_count.get(char, 0) + 1
    for c in alpha_count:
        print(f"The letter '{c}' was found {alpha_count[c]} times")

main()

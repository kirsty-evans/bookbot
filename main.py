from stats import get_num_words
import sys

def sort_key(dict):
    return dict["count"]

def count_char(text):
    print("--------- Character Count -------")
    lowercase = text.lower()
    dictionary = {}
    for character in lowercase:
        if character.isalpha():
            if character not in dictionary:
                dictionary[character] = 1
            else:
                dictionary[character] += 1
    converted_list = []
    for item in dictionary:
        newdict = {"letter":item, "count": dictionary[item]}
        converted_list.append(newdict)
    converted_list.sort(reverse=True, key = sort_key)

    for item in converted_list:
            print(f"{item["letter"]}: {item["count"]}")

def main():

    # the first argument should be the path to the book, e.g. 'books/frankenstein.txt'

    # arguments check
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) #exit with error code 1

    selected_book = sys.argv[1]

    with open(selected_book) as f:
        file_contents = f.read()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {selected_book}...")
    get_num_words(file_contents)
    count_char(file_contents)
    print("--- End report ---")

main()
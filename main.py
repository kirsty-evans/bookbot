from stats import get_num_words

def sort_key(dict):
    return dict["count"]

def count_char(text):
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
            print(f"The '{item["letter"]}' character was found {item["count"]} times")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"--- Begin report of books/frankenstein.txt ---")
    get_num_words(file_contents)
    count_char(file_contents)
    print("--- End report ---")

main()
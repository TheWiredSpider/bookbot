def get_word_count(file):
    word_list = []
    word_list = file.split()
    return len(word_list)



def get_character_count(file):
    char_dict = {}
    dict_list = []
    for char in file.lower():
        if char.isalpha():
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1

    for item in char_dict:
        dict_list.append({"name":item, "num":char_dict[item]})
            
    def sort_on(dict):
        return dict["num"]

    dict_list.sort(reverse = True, key = sort_on)
    return dict_list


def main():
    print("-- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = get_word_count(file_contents)
    print(f"{word_count}  words found in the document")
    print("")
    char_count = get_character_count(file_contents)

    for item in char_count:
        print(f"The '{item['name']}' character was found {item['num']} times")

    print("--- End report ---")
main()

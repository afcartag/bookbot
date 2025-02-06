with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    #finds and prints nubmer of words in doc
    print(wordcounter(file_contents), "words found in the document\n")
    #stores character count in dictionary
    characters = character_counter(file_contents)
    #converts dictionary into list of dictionaries with only letters
    letters = letter_counter(characters)
    #returns
    aggregated_report(letters)
    print("--- End report ---")

def wordcounter(book):
    words = book.split()
    wordcount=0

    for word in words:
        wordcount += 1
    return wordcount


def character_counter(book):
    character_count = {}
    my_book = book.lower()
    for char in my_book:
        if char not in character_count:
            character_count[char] = 1
        elif char in character_count:
            character_count[char] +=1
    return character_count

def letter_counter(book):
    letters = []
    for letter in book:
        if letter.isalpha() == True:
            letter_count = {'letter':letter, 'count':book[letter]}
            letters.append(letter_count)
    return letters

def aggregated_report(list_of_dicts):
    list_of_dicts.sort(reverse=True, key=sort_on)
    for i in list_of_dicts:
        print(f"The '{i["letter"]}' character was found {i["count"]} times")
    
def sort_on(dict):
    return dict['count']

if __name__ == "__main__":
    main()
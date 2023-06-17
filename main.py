import random
import json


words_file = "assets/words.json"


settings = ""
with open("settings.json", 'r') as f:
    settings = json.load(f)

placeholder = settings["placeholder"]
min_len = settings["min_len"]
max_len = settings["max_len"]


def chooseWord(wordsFile, min_len, max_len):
    with open(wordsFile, 'r') as f:
        file = json.load(f)

        entry = random.choice(file)
        while max_len < len(entry["word"]) or min_len > len(entry["word"]):
            entry = random.choice(file)
        word_chosen = entry["word"]
        definition = entry["definition"]
    return [word_chosen, definition]


def getfinal(word, indexes, placeholder):
    final_word = ""
    for i in range(len(word)):
        current = word[i]
        if i in indexes:
            final_word += current
        else:
            final_word += placeholder
    return final_word


def findindex(word, letter):
    arr = []
    for i in range(len(word)):
        if letter == word[i].lower():
            arr.append(i)
    return arr


def arrayAppend(arrayA, arrayB):
    final = []
    for i in arrayA:
        final.append(i)
    for i in arrayB:
        final.append(i)
    return final


def play(word):
    user_final = getfinal(word, [], placeholder)
    final_indexes = []
    while user_final != word:
        print(user_final)

        user_letter = input("Place your guess ").lower()

        if user_letter == word:
            user_final = word
            break
        a = findindex(word, user_letter)
        final_indexes = arrayAppend(final_indexes, a)
        user_final = getfinal(word, final_indexes, placeholder)
    print(user_final)
    print("Congratulations, you won!")


word_chosen = chooseWord(words_file, min_len, max_len)
play(word_chosen[0])

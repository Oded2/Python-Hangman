import random
import json


words_file = "assets/words.json"


settings = ""
with open("settings.json", 'r') as f:
    settings = json.load(f)

placeholder = settings["placeholder"]
min_len = settings["min_len"]
max_len = settings["max_len"]
max_tries = settings["max_tries"]
hints = settings["hints"]


def enterToContinue():
    input("Press ENTER to continue ")


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


def arrayStringify(arr):
    final = ""
    for i in range(len(arr)):
        current = arr[i]
        if i == len(arr)-1:
            final += str(current) + " "
        else:
            final += str(current) + ", "

    return final


def play(wordArr, tries):
    word = wordArr[0]
    definition = wordArr[1]
    user_final = getfinal(word, [], placeholder)
    final_indexes = []
    letters_used = []
    ogTries = tries

    while user_final != word:

        print(user_final)
        if len(letters_used) != 0:
            print(f"Incorrect Letters: {arrayStringify(letters_used)}")
        print(f"Tries left: {tries}")
        if tries == int(ogTries/3) and hints:
            print(f"The definition is {definition}")
        if tries == 0:
            print(f'You failed, the word was "{word}"')
            enterToContinue()
            exit()

        user_letter = input("Place your guess ").lower()
        if user_letter not in word:
            if user_letter not in letters_used:
                tries -= 1
                letters_used.append(user_letter)
            else:
                print(f'You gussed the letter "{user_letter}".')
        if user_letter == word:
            user_final = word
            break
        a = findindex(word, user_letter)
        final_indexes = arrayAppend(final_indexes, a)
        user_final = getfinal(word, final_indexes, placeholder)

    print(user_final)
    print("Congratulations, you won!")


word_chosen = chooseWord(words_file, min_len, max_len)
play(word_chosen, max_tries)
enterToContinue()

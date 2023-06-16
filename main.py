import random

words = ["zebra", "alpha", "pinkie"]
word_chosen = random.choice(words)


def getfinal(word, indexes):
    final_word = ""
    for i in range(len(word)):
        current = word[i]
        if i in indexes:
            final_word += current
        else:
            final_word += "_"
    return final_word

# getfinal("hello", 2)
# >> __l__


def findindex(word, letter):
    arr = []
    for i in range(len(word)):
        if letter == word[i]:
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
    user_final = getfinal(word, [])
    final_indexes = []
    while user_final != word:
        print(user_final)

        user_letter = input("Place your guess ")

        if user_letter == word:
            user_final = word
            break
        a = findindex(word, user_letter)
        final_indexes = arrayAppend(final_indexes, a)
        user_final = getfinal(word, final_indexes)
    print(user_final)
    print("Congratulations, you won!")


play(word_chosen)

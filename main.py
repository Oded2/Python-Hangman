import random

words = ["zebra", "alpha", "pinkie"]
word_chosen = random.choice(words)

def play(word):
    user_letter = input("Place your first guess")
    if user_letter in word:
        pass
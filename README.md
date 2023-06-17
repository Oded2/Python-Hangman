# Hangman Game

This is a simple hangman game implemented in Python. The game randomly selects a word from a provided list of words and gives you a limited number of tries to guess the word correctly. 

## Prerequisites

- Python 3

## Installation

1. Clone the repository or download the `main.py` file.
2. Customize the game settings in the *settings.json* file if desired.

## How to Play

1. Run the *main.py* file using Python.
2. The game will start by displaying a placeholder word with underscores representing the letters.
3. Enter your guesses one letter at a time.
4. If your guess is incorrect, the game will display the incorrect letters and the number of tries remaining.
5. If your guess is correct, the game will reveal the correct letters in the placeholder word.
6. Keep guessing until you either guess the word correctly or run out of tries.
7. If you guess the word correctly, you win the game.
8. If you run out of tries, the game ends and reveals the correct word.

## Game Customization

You can customize the game settings by modifying the *settings.json* file. The available settings are:

- *placeholder*: The character used to represent unknown letters in the placeholder word.
- *min_len*: The minimum length of the word to be chosen.
- *max_len*: The maximum length of the word to be chosen.
- *max_tries*: The maximum number of tries allowed.
- *hints*: A boolean value indicating whether to provide hints by displaying the word's definition.

Feel free to modify these settings to adjust the difficulty or gameplay experience of the game.

## Credits

The game uses a list of words stored in the *words.json* file. The words and their definitions are sourced from an external database.

## License

This project is licensed under the *MIT License*. Feel free to modify and distribute it according to the terms of the license.

For more information, see the *LICENSE* file.

---

Have fun playing the hangman game! If you have any further questions, feel free to ask.

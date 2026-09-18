
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a word-guessing game that uses Python strings, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️ Select a Secret Word

#### Description
Create a list of possible words and randomly select one word for the player to guess.

#### Requirements
Completed program should:

- Store multiple possible words in a predefined list.
- Use Python's `random` module to select one secret word.
- Keep the selected word hidden from the player during the game.

### 🛠️ Build the Guessing Loop

#### Description
Allow the player to guess letters and reveal their progress until the word is complete or the player runs out of attempts.

#### Requirements
Completed program should:

- Display the current progress using underscores for letters that have not been guessed, such as `_ _ _`.
- Accept a letter guess from the player.
- Reveal every matching letter in the secret word.
- Track incorrect guesses and reduce the number of remaining attempts.
- Continue playing until the word is guessed or no attempts remain.

### 🛠️ Display the Game Result

#### Description
End the game with a clear message that tells the player whether they won or lost.

#### Requirements
Completed program should:

- Display a win message when all letters in the secret word are revealed.
- Display a lose message when the player runs out of incorrect guesses.
- Reveal the secret word when the player loses.

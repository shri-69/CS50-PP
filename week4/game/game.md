# 🎲 Guessing Game - CS50 Python Project

`game.py` is a simple number-guessing game written in Python. The program generates a secret number and asks the user to guess it, providing hints until the user gets it *Just right!* 🧠

---

## 📁 File

- `game.py`

---

## 📝 Description

This program:

1. Prompts the user for a **level** (a positive integer), which determines the upper bound of the random number to guess.
2. Randomly selects an integer between `1` and the chosen `level`.
3. Continuously prompts the user to **guess the number**:
   - If the guess is **too small**, it says `"Too small!"`
   - If the guess is **too large**, it says `"Too large!"`
   - If the guess is **correct**, it says `"Just right!"` and exits.

---

## 🎮 Sample Run
Level: 50
Guess: 25
Too small!
Guess: 45
Too large!
Guess: 37
Just right!


---

## 🛠️ Usage

Run the program using Python:

```bash
python game.py

Follow the prompts:
- First, enter a level (positive integer).
- Then, start guessing the number.


✅ Input Validation
The program ensures:
- The level is a positive integer.
- The guesses are positive integers.
- It keeps prompting until valid input is provided.


📦 Modules Used
- random: For generating the secret number.


👨‍💻 Author
Project for CS50’s Introduction to Computer Science
by [SHRIYA DHAWAN]

📄 License
Free to use for educational and personal development purposes.


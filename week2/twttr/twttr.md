### 🐦 Twttr - Vowel Omission Program

This Python script simulates the classic social media trend of shortening words by omitting vowels, inspired by how “Twitter” was originally stylized as “twttr”. It is a beginner-friendly program that takes a string input from the user and returns the same string with all vowels removed.

## 💡 Problem Description

When texting, tweeting, or writing informally, people often omit vowels to save space or type faster. For example:
- `hello` becomes `hll`
- `Twitter` becomes `Twttr`
- `beautiful` becomes `btfl`

This program:
- Prompts the user for a line of text
- Removes all **vowels**: `a`, `e`, `i`, `o`, `u` (case-insensitive)
- Outputs the modified string with vowels omitted

## 🧠 Logic

The core of the program is a loop that:
- Iterates through each character in the input string
- Checks whether the character is a vowel (upper or lowercase)
- If it’s **not a vowel**, the character is added to a new string
- Finally, it prints the shortened version of the string

## 🖥 Example Run

Input: Twitter is amazing!
Output: Twttr s mzng!



## 📄 Files

- `twttr.py`: Main Python script that performs the vowel omission

## ✅ How to Run

Make sure you have Python installed. Then, in the terminal:

```bash
python twttr.py


📚 Learning Outcomes
This simple project helps you practice:

String manipulation

Using for loops and conditionals

Character filtering

Working with case sensitivity in Python

It’s a great exercise to build confidence in text processing and control flow logic for beginners.

🏁 License
This project was created as part of the CS50 Python curriculum. Feel free to use and adapt it for learning or teaching purposes.



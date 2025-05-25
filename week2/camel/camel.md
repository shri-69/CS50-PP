### 🐫 CamelCase to Snake_Case Converter

This Python program converts variable names from **camelCase** (commonly used in languages like JavaScript and Java) to **snake_case**, which is the preferred naming convention in Python.

## 💡 Problem Description

In camel case, multiple words are written together without spaces, and each word after the first begins with a capital letter:
- `firstName`
- `preferredFirstName`

In contrast, Python uses **snake case**, in which all letters are lowercase and words are separated by underscores:
- `first_name`
- `preferred_first_name`

The task is to write a program that:
- Prompts the user to input a camelCase variable name
- Converts it into snake_case
- Outputs the result

## 🧠 Logic

The program loops through each character in the input string:
- If the character is **uppercase**, it:
  - Adds an underscore `_` to the `snake` variable
  - Appends the lowercase version of the character
- If the character is lowercase, it appends it as-is

## 🖥 Example

camelCase: preferredFirstName
snake_case: preferred_first_name


## 📄 File Structure

- `camel.py`: The main Python file that contains the program.

## ✅ How to Run

Make sure you have Python installed. Then, from your terminal or command prompt:

```bash
python camel.py


📚 Learning Outcomes
By completing this project, you will strengthen your understanding of:

String manipulation in Python

Control flow using for loops and conditionals

Working with character cases and ASCII values

Writing beginner-friendly command-line applications

This is a great exercise for anyone learning Python and becoming familiar with naming conventions across different programming languages.

🏁 License
This project is created for educational purposes as part of CS50’s Python curriculum. You are free to use, modify, and share it for learning.
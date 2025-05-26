# 😀 Emojize - CS50 Python Project

`emojize.py` is a simple Python program that converts emoji codes or aliases into actual emoji characters using the `emoji` Python library. This is particularly useful when typing emoji on devices where inserting graphical emoji directly is difficult.

---

## 📁 File

- `emojize.py`

---

## 📝 Description

This program:

- Prompts the user to enter a string.
- Replaces all recognized emoji codes or aliases (e.g., `:thumbs_up:` or `:thumbsup:`) with the actual emoji (👍).
- Uses the `emoji` library's alias mode to support both standard and alias codes.

---

## 🛠️ Dependencies

Install the `emoji` package using pip if you haven’t already:

```bash
pip install emoji

▶️ How to Run
python emojize.py
You’ll be prompted to enter a string with emoji codes:

Enter your text: I love Python! :snake: :thumbsup:
Emojized text:
I love Python! 🐍 👍


✅ Features
- Supports both emoji codes (:thumbs_up:) and aliases (:thumbsup:).
- Utilizes the emoji.emojize() function with language='alias' to ensure broad compatibility.
- Great practice for string processing and working with external libraries in Python.


🔗 Emoji Code Reference
Check out all available emoji codes and their aliases here:
https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias


📌 Example Inputs & Outputs
Input:
Enter your text: Hello, world! :earth_americas:

Output:
Emojized text:
Hello, world! 🌎

👨‍💻 Author
Project for CS50’s Introduction to Computer Science
by [SHRIYA DHAWAN]

📜 License
Free to use for educational and non-commercial purposes.

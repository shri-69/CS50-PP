# 🎨 Figlet - CS50 Python Project

`figlet.py` is a Python program that converts text into ASCII art using fonts from the `pyfiglet` library, a Python port of the classic FIGlet program.

---

## 📁 File

- `figlet.py`

---

## 📝 Description

This program:

- Accepts either **zero or two command-line arguments**.
- Prompts the user for a string of text.
- Outputs the text as ASCII art using a specified or random font.

---

## 🛠️ Features

- 🎲 Random font mode (if no arguments are passed).
- 🎨 Custom font mode (using `-f` or `--font` followed by a valid font name).
- 📤 Outputs large ASCII-art style text in terminal.
- ⚠️ Handles invalid inputs and unknown fonts gracefully using `sys.exit()`.

---

## 🔧 Usage

### 1. Output with a random font:
```bash
python figlet.py

2. Output with a specific font:
python figlet.py -f slant
or 
python figlet.py --font slant

Then you’ll be prompted to enter a string:
Enter text to display: Hello CS50!


📦 Dependencies
Install pyfiglet before running the script:
pip install pyfiglet

📜 Example
$ python figlet.py -f standard
Enter text to display: CS50
   ____ ____  _____ ____  
  / ___|  _ \| ____|  _ \ 
 | |   | |_) |  _| | | | |
 | |___|  __/| |___| |_| |
  \____|_|   |_____|____/ 


🧠 Error Handling
❌ Invalid flag:
Error: Invalid flag. Use -f or --font to specify a font.

❌ Unknown font:
Error: Font not found. Please choose a valid font name.

❌ Incorrect usage:
Usage: python figlet.py OR python figlet.py -f <fontname>


👨‍💻 Author
Project for CS50’s Introduction to Computer Science
by [SHRIYA DHAWAN]

📄 License
Free to use for learning and academic purposes.


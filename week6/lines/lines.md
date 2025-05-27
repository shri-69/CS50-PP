# 📏 Line Counter – Python LOC Analyzer

`lines.py` is a command-line Python utility that analyzes a `.py` file and counts the number of actual **lines of code (LOC)**, excluding **comments** and **blank lines**. This tool helps estimate the size or simplicity of Python programs.

---

## 📁 File

- `lines.py`

---

## 📝 Description

This script:

- Accepts exactly **one command-line argument**: the path to a `.py` file.
- Exits with an error if:
  - The argument count is incorrect.
  - The file does **not end with `.py`**.
  - The file **does not exist**.
- Counts only **lines that are actual code**:
  - Ignores lines starting with `#`, even if preceded by spaces or tabs (i.e., comments).
  - Ignores **blank lines** or those containing only whitespace.
  - **Docstrings** (multi-line string literals) are **not** considered comments.

---

## ✅ Example

### Sample file: `example.py`
```python
# Say hello

name = input("What's your name? ")
print(f"hello, {name}")

Run:
$ python lines.py example.py
2
Only two lines are counted — the comment and blank line are excluded.

🛠️ Requirements
- Python 3

📦 Usage
- python lines.py <filename>.py

Example:
python lines.py script.py

💡 Educational Objectives
This project helps practice:
- File I/O operations
- Command-line argument parsing with sys
- String manipulation and whitespace handling
- Error handling with sys.exit()
- Basic program complexity analysis techniques

📂 Error Handling
Scenario	                                    Message
No argument or too many arguments	            Usage: python lines.py filename.py
Non-.py file	                                Error: Not a Python file (must end with .py)
File doesn't exist	                          Error: File 'filename.py' does not exist
File read failure	                            Error reading file: <specific message>

👨‍💻 Author
Project for CS50’s Introduction to Computer Science
by [SHRIYA DHAWAN]

📄 License
Free for educational and non-commercial use.

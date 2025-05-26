# 🧮 Math Expression Interpreter (Python)

This is a simple Python interpreter that takes user input in the form of a basic arithmetic expression and evaluates it.  
The program supports addition, subtraction, multiplication, and division using standard mathematical symbols.

---

## 📄 File

- `interpreter.py`

---

## 🔍 What It Does

Prompts the user to enter an arithmetic expression in the format:
x y z


Where:
- `x` is an integer (first operand)
- `y` is an operator (`+`, `-`, `*`, or `/`)
- `z` is an integer (second operand)

Then, it evaluates the result and prints it as a **floating-point number** rounded to **one decimal place**.

---

## 🧮 Supported Operations

| Operator | Operation     |
|----------|---------------|
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |

---

## 📥 Example Usage

```bash
$ python interpreter.py
Enter math expression (e.g. 3 + 4): 7 * 5
35.0

$ python interpreter.py
Enter math expression (e.g. 3 + 4): 10 / 4
2.5

🧠 Assumptions
Input will always be in the correct format: x y z
x and z are integers
y is a valid operator: +, -, *, or /
Division by zero is not allowed (assumed to never occur)

🚀 How to Run
Make sure you have Python 3 installed, then run:
python interpreter.py

📜 License
This project is free for educational and personal use.

✍️ Author
[SHRIYA DHAWAN]


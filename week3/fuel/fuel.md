# ⛽ Fuel Gauge (Python)

This Python program simulates a fuel gauge by converting a user-inputted fraction (e.g., `3/4`) into a percentage that represents how full a fuel tank is.

---

## 📄 File

- `fuel.py`

---

## 🔍 What It Does

The program:

1. Prompts the user to input a fuel fraction in the format `X/Y`, where both `X` and `Y` are integers.
2. Calculates the percentage of fuel remaining.
3. Rounds the result to the nearest whole number.
4. Prints:
   - `E` if the percentage is **1% or less** (empty).
   - `F` if the percentage is **99% or more** (full).
   - The actual percentage (e.g., `75%`) for values in between.

It will **repeatedly prompt** the user until valid input is provided.

---

## ✅ Example Behavior

```bash
$ python fuel.py
How much fuel? (format X/Y): 3/4
75%

$ python fuel.py
How much fuel? (format X/Y): 1/100
E

$ python fuel.py
How much fuel? (format X/Y): 99/100
F


💡 Features
Handles edge cases:
Prevents division by zero.
Ensures X <= Y.
Requires both X and Y to be integers.
Loops until valid input is given.
Rounds the percentage for more realistic output.


⚠️ Error Handling
- ValueError: If the input format is wrong (not X/Y) or if X or Y is not an integer.
- ZeroDivisionError: If Y (the denominator) is 0.

🚀 How to Run
Make sure you have Python 3 installed, then run the program:
python fuel.py

📜 License
Free to use for educational purposes.

✍️ Author
[SHRIYA DHAWAN]

# 🍕 Pizza Menu Formatter

**`pizza.py`** is a Python program that reads a pizza menu from a CSV file (in the style of Pinocchio’s Pizza & Subs at Harvard Square) and prints it as a well-formatted **ASCII table** using the `tabulate` library.

---

## 📁 File

- `pizza.py`

---

## 🧾 Description

This script:

- Accepts **exactly one** command-line argument: the **path to a `.csv` file**.
- Validates that the file:
  - Has a `.csv` extension.
  - Exists in the file system.
- Uses the **`tabulate`** library to output the data in a neat table using the `"grid"` format.

---

## 📋 Example Input (CSV)

Sample: `sicilian.csv`
```csv
Sicilian Pizza,Small,Large
Cheese,$25.50,$39.95
1 item,$27.50,$41.95
2 items,$29.50,$43.95
3 items,$31.50,$45.95
Special,$33.50,$47.95

📤 Example Output
$ python pizza.py sicilian.csv
+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+

🛠 Requirements
- Python 3
- tabulate package
- Install via pip:
    pip install tabulate

🚀 Usage
python pizza.py <filename>.csv

Example:
python pizza.py sicilian.csv


❌ Error Handling
Situation	Message
No argument provided	Usage: python pizza.py data.csv
File extension not .csv	Error: File must be a .csv file
File not found	Error: File 'filename.csv' not found
File is empty	Error: CSV file is empty
Other file read issues	Error while reading the file: <details>

📚 Educational Objectives
Practice file and argument validation using sys and os
Work with CSV files using the csv module
Improve data presentation using third-party packages
Gracefully handle user errors

👨‍💻 Author
Project for CS50’s Introduction to Computer Science
by [SHRIYA DHAWAN]

📄 License
Free for educational and non-commercial use.

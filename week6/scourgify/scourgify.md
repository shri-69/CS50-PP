# 🧹 Scourgify

**`scourgify.py`** is a Python program that "cleans" messy CSV data from Hogwarts by splitting full names into separate **first** and **last** columns, making it easier for tasks like mail merges.

Inspired by the spell **Scourgify**, which cleans physical messes in the wizarding world, this program cleans **data** messes in the muggle world.

---

## 📁 Files

- `scourgify.py`
- Input file: `before.csv` (sample format provided below)
- Output file: `after.csv` (will be created by the script)

---

## 🧾 Description

The script:

1. Accepts **two command-line arguments**:
   - The input `.csv` file to read (e.g., `before.csv`)
   - The output `.csv` file to write (e.g., `after.csv`)
2. Parses each row in the input, where names are formatted as `"Last, First"`.
3. Writes a new CSV file with three columns: `first`, `last`, and `house`.

---

## 📥 Sample Input (`before.csv`)

```csv
name,house
"Potter, Harry",Gryffindor
"Granger, Hermione",Gryffindor
"Weasley, Ron",Gryffindor
"Malfoy, Draco",Slytherin

📤 Sample Output (after.csv)
- first,last,house
- Harry,Potter,Gryffindor
- Hermione,Granger,Gryffindor
- Ron,Weasley,Gryffindor
- Draco,Malfoy,Slytherin

🚀 Usage
  python scourgify.py input.csv output.csv

Example:
python scourgify.py before.csv after.csv


❌ Error Handling
Situation	                                                       Error Message
Wrong number of arguments	                                        Usage: python scourgify.py input.csv output.csv
Input file not found	                                            Error: File 'input.csv' not found
Input file unreadable or malformed	                              Something went wrong while reading the input file: <details>
Output file cannot be written	                                    Couldn’t write to output file: <details>

🧠 Learning Objectives
Practice with CSV reading/writing using Python’s csv module
Learn how to split and reformat string data
Handle file-related exceptions gracefully with try/except
Use sys.argv for command-line input
Ensure code is modular and robust

📦 Requirements
Python 3.x
(No external libraries needed)

🧙‍♂️ Author
Inspired by CS50's Introduction to Python programming.
By [SHRIYA DHAWAN]

📄 License
MIT License. Free to use for educational purposes.

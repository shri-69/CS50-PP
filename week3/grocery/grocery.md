# 🛒 Grocery List Tracker (Python)

This is a simple Python command-line program that allows users to build a grocery list interactively by entering items one at a time. It counts how many times each item is added and displays the full list in uppercase and sorted order when the input ends.

---

## 📄 File

- `grocery.py`

---

## 🧠 How It Works

- Prompts the user to input grocery items **one per line**.
- Accepts inputs **case-insensitively** (e.g., `apple`, `Apple`, `APPLE` are treated the same).
- Stores and counts the number of times each item is entered.
- Ends input when the user presses **Ctrl-D** (EOF).
- Outputs the full list of items in **uppercase**, **sorted alphabetically**, each prefixed by its count.

---

## ✅ Sample Interaction

```bash
$ python grocery.py
apple
banana
apple
milk
Banana
<Ctrl-D>

2 APPLE
2 BANANA
1 MILK

📌 Features
- Uses a Python dictionary to count occurrences of each item.
- Case-insensitive handling of item input.
- Outputs the final list in a clean, sorted, and readable format.
- Does not pluralize items (e.g., still prints APPLE for multiple apples).


🚀 How to Run
Make sure you have Python 3 installed. Then run the program in your terminal:
python grocery.py

Input your grocery items line by line. When you're done, press CTRL+D or CTRL+Z then Enter to end input and display the list.

⚠️ Notes
- Input should be provided via standard input (keyboard).
- The program terminates and prints the list upon receiving an EOF signal.


📜 License
Free to use for educational and non-commercial purposes.

✍️ Author
[SHRIYA DHAWAN]


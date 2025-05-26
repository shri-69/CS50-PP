# 🌮 Taqueria Ordering System (Python)

This is a simple Python-based command-line application that allows users to simulate placing an order at Felipe’s Taqueria in Harvard Square. The user is prompted to enter items one by one, and the running total of the order is displayed after each valid entry.

---

## 📄 File

- `taqueria.py`

---

## 📋 Menu

```python
{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


🧠 How It Works
- Prompts the user repeatedly to enter the name of an item.
- Accepts item names case-insensitively (e.g., burrito, BURRITO, and Burrito are all valid).
- Ignores invalid or unrecognized items.
- Keeps a running total of the order, displaying it after each valid entry.
- Ends input when the user presses Ctrl-D (EOF), then displays the final total.

⚙️ Features
- Case-insensitive matching of menu items.
- Clean formatting with totals shown in two decimal places.
- Handles unknown items gracefully by ignoring them.
- Uses EOFError handling to detect order completion via Ctrl-D.

🚀 How to Run
Make sure you have Python 3 installed. Run the program using:
python taqueria.py
Press Ctrl-D to finish your order.


📜 License
Free to use and modify for educational purposes.

✍️ Author
[SHRIYA DHAWAN]




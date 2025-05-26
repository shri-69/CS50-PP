# 💸 Tip Calculator (Python)

This simple Python program calculates the tip amount you should leave based on your meal's cost and desired tip percentage. It processes common dollar and percent input formats such as `$50.00` and `15%`.

---

## 📄 File

- `tip_calculator.py`

---

## 📥 How It Works

1. The user is prompted to enter:
   - **Meal cost** in dollars (e.g., `$50.00`)
   - **Tip percentage** (e.g., `15%`)

2. The program:
   - Converts dollar and percent strings to `float`
   - Calculates the tip amount
   - Displays it formatted to 2 decimal places

---

## 🧮 Example

```bash
$ python tip_calculator.py
How much was the meal? $100.00
What percentage would you like to tip? 20%
Leave $20.00

💡 Functions
- dollars_to_float(d)
  Converts input like $50.00 → 50.0

- percent_to_float(p)
 Converts input like 15% → 0.15


🚀 Run the Program
Make sure you have Python 3 installed. Then run:
python tip_calculator.py


🧠 Requirements
Python 3.x

📜 License
This project is free to use and modify for educational or personal purposes.





# 🍽️ Meal Time Checker (Python)

This is a simple Python program that helps you figure out whether it's **breakfast**, **lunch**, or **dinner** time based on the current time you input.  
It interprets the time and tells you what meal you should be having (if any).

---

## 📄 File

- `meal.py`

---

## 🔍 What It Does

Prompts the user to enter the current time in **24-hour format** (e.g., `7:30`, `12:00`, `18:45`) and checks whether the time falls within one of the typical meal windows:

| Meal      | Time Range (Inclusive) |
|-----------|-------------------------|
| Breakfast | 07:00 – 08:00           |
| Lunch     | 12:00 – 13:00           |
| Dinner    | 18:00 – 19:00           |

If the time is within a meal time range, it prints the appropriate message.  
If it's outside those ranges, the program prints nothing.

---

## 🧠 How It Works

### `convert(time: str) -> float`

- Converts time from `"HH:MM"` format into a float.
- Example: `"7:30"` → `7.5`

### `main()`

- Gets user input.
- Converts the input time to float using `convert()`.
- Checks which meal window the time falls into.

---

## 📥 Example Usage

```bash
$ python meal.py
What time is it? 7:00
breakfast time

$ python meal.py
What time is it? 12:59
lunch time

$ python meal.py
What time is it? 15:30
# (No output, as it’s not a meal time)

✅ Assumptions
- Time will always be entered in H:MM or HH:MM format (24-hour clock).
- Input is assumed to be valid (no error handling needed for incorrect formats).

🚀 How to Run
Make sure you have Python 3 installed, then run the script:
python meal.py

📜 License
Free for educational and personal use.

✍️ Author
[SHRIYA DHAWAN]





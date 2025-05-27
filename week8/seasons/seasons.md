# ⏳ seasons.py — How Many Minutes Since You Were Born?

This Python script calculates the **total number of minutes** that have passed since your birth date (assuming midnight), and prints the result **in English words**, inspired by the song *"Seasons of Love"* from *Rent*.

> “Five hundred twenty-five thousand six hundred minutes…”

---

## 📌 Features

- Accepts birthdate input in `YYYY-MM-DD` format.
- Calculates total **minutes** from **midnight of your birthdate to today at midnight**.
- Converts the number into **English words**, using the [`inflect`](https://pypi.org/project/inflect/) library.
- Handles invalid inputs gracefully by exiting with an error message.

---

## 🧮 Example

### Input:
Date of Birth (YYYY-MM-DD): 2000-01-01

### Output:
Thirteen million two hundred seventy-nine thousand four hundred forty minutes


---

## 🧠 How It Works

1. The user is prompted to enter their **birthdate**.
2. The program:
   - Parses the date.
   - Calculates the number of **days** from birth until today using `datetime.date.today()`.
   - Converts days into **minutes**: `days × 24 × 60`.
   - Converts that integer to **English words** using `inflect`.
3. If the date is malformed, the program exits with an error.

---

## 📁 File Structure
├── seasons.py # Main program
├── test_seasons.py # Unit tests for get_minutes_since_birth
└── README.md # This file


---

## 🧪 Testing

Unit tests are written in `test_seasons.py`. Only the helper function `get_minutes_since_birth()` is tested, not `main()`.

### Example `test_seasons.py`:

```python
from seasons import get_minutes_since_birth
from datetime import date

def test_minutes_today():
    today = date.today().strftime("%Y-%m-%d")
    assert get_minutes_since_birth(today) == 0

def test_minutes_yesterday():
    from datetime import timedelta
    yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    assert get_minutes_since_birth(yesterday) == 1440  # 24 * 60

def test_invalid_format():
    import pytest
    with pytest.raises(ValueError):
        get_minutes_since_birth("01-01-2000")

Run tests with:
pytest test_seasons.py

🧑‍💻 Requirements
Python 3
inflect package

Install dependencies:
pip install inflect

💡 Tip
Even if the current time is 3:00 PM, the program assumes it's midnight today, for both simplicity and consistency.

📜 License
This script is released under the MIT License. Use it, learn from it, and remix it!

✨ Inspired By
This project is inspired by CS50P, a Python programming course by Harvard.

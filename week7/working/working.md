# 🕒 working.py — 12-Hour to 24-Hour Time Converter

This Python script allows you to convert **12-hour formatted times** (with AM/PM) into **24-hour formatted times** (HH:MM). It supports common variants used in American English time ranges such as:

- `9:00 AM to 5:00 PM`
- `9 AM to 5 PM`
- `9:00 AM to 5 PM`
- `9 AM to 5:00 PM`

---

## ✅ What It Does

Given input like:
Hours: 9 AM to 5 PM
It returns:
09:00 to 17:00


---

## ⚙️ How It Works

- Uses regular expressions (`re`) to validate and extract hour, minute, and meridiem components.
- Converts the 12-hour format to 24-hour format using custom logic:
  - `12 AM` becomes `00:00`
  - `12 PM` remains `12:00`
  - Other AM hours remain unchanged
  - Other PM hours have 12 added to the hour

---

## 🔎 Validation Rules

The script will raise a `ValueError` if:
- The input does not match expected 12-hour formats
- The hour is not in `1–12` range
- The minutes are not in `0–59` range

Examples of invalid inputs:
- `13:00 PM to 5:00 PM`
- `12:60 AM to 1 PM`
- `9:00AMto5:00PM`

---

## 🧪 Testing

To ensure correctness, you can write tests in `test_working.py` using `pytest`.

### Example Test Functions:

```python
from working import convert
import pytest

def test_full_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_hour_only():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_mixed_formats():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

def test_midnight_and_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_invalid_times():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("random text")


Run tests with:
pytest test_working.py

📝 Usage
python working.py

Sample interaction:
Hours: 7:30 AM to 6:15 PM
07:30 to 18:15


📁 File Structure
├── working.py        # Main program
├── test_working.py   # Unit tests
└── README.md         # Documentation

👨‍💻 Author
Created as part of Harvard’s CS50P problem sets — focused on string parsing and time conversion logic in Python.

📜 License
MIT License — feel free to use and adapt.

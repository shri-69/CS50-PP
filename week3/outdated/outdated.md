# 📅 Outdated Date Formatter

This Python command-line program prompts the user to enter a date in a **US-friendly format** like `MM/DD/YYYY` or `Month DD, YYYY` (e.g., `9/8/1636` or `September 8, 1636`) and then converts it to the internationally preferred **ISO 8601 format**: `YYYY-MM-DD`.

---

## 🗃️ File

- `outdated.py`

---

## 🧠 How It Works

- Prompts the user to input a date.
- Accepts:
  - Numeric date: `MM/DD/YYYY`
  - Textual date: `Month DD, YYYY` (e.g., `October 3, 2005`)
- Validates:
  - Month is between 1 and 12 or a recognized month name.
  - Day is between 1 and 31 (does not check for month-specific days like 28, 30, etc.).
- Converts and outputs the date in `YYYY-MM-DD` format with zero-padded values.
- If the input is invalid, the user is prompted again.

---

## ✅ Sample Usage

```bash
$ python outdated.py
Date: September 8, 1636
1636-09-08


$ python outdated.py
Date: 3/14/2000
2000-03-14

$ python outdated.py
Date: wrong input
Date: 10/3/1999
1999-10-03


🌍 Why This Matters
- Most databases and programming environments use ISO 8601 format (YYYY-MM-DD) because it is:
- Unambiguous
- Easily sortable
- Standardized across systems and regions
This program helps convert messy, user-friendly formats into clean, machine-friendly ones.


🚀 How to Run
Make sure you have Python 3 installed, then run:
python outdated.py

Enter your date in the prompted format. If the format is incorrect, the program will keep asking until a valid input is provided.


📌 Notes
- Input is case-sensitive for month names. (e.g., September is valid, but september is not)
- Handles both /-separated and Month DD, YYYY inputs.
- Doesn’t validate leap years or exact number of days per month — all months are assumed to allow up to 31 days.

📜 License
This project is open-source and free to use for educational and non-commercial use.

✍️ Author
[SHRIYA DHAWAN]

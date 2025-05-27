# 👋 Adieu - CS50 Python Project

`adieu.py` is a Python program that prompts the user for names and then bids them farewell in the spirit of the classic *"So Long, Farewell"* song from *The Sound of Music* — with proper comma placement and the Oxford comma!

---

## 📁 File

- `adieu.py`

---

## 📝 Description

This program:

- Prompts the user to enter names one by one.
- Accepts input until the user sends an EOF signal (Ctrl-D on macOS/Linux, Ctrl-Z on Windows).
- Outputs a farewell string formatted with commas and the word "and" correctly according to how many names were entered.

---

## 📤 Example Output

For example, if the input is:
Liesl
Friedrich
Louisa
Kurt
Brigitta
Marta
Gretl

Then the output will be:
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl


---

## 🧠 Logic

The program uses Python’s `join()` method to format the names:
- **1 name**: `Adieu, adieu, to Liesl`
- **2 names**: `Adieu, adieu, to Liesl and Friedrich`
- **3+ names**: Uses Oxford comma style — `X, Y, and Z`

---

## 🛠️ Usage

Run the program using Python:

```bash
python adieu.py

Then type names one per line. Press CTRL+D to stop.


🛑 Edge Case
If no names are entered, the program exits with an error message:
No names entered... but you said you'd enter at least one!

👨‍💻 Author
Project for CS50’s Introduction to Computer Science
by [SHRIYA DHAWAN]

📄 License
Free to use for academic and personal learning purposes.

# 🗣️ um.py — Count the "Um"s

This Python script counts how many times the word **"um"** appears in a given string of text. It matches only **standalone "um"**, not when it appears as a part of another word (like “yummy” or “umbrella”), and it is **case-insensitive**.

---

## ✅ What It Does

- Accepts a line of text input.
- Returns the number of times **"um"** appears as a **whole word**, ignoring case.

### Examples:

| Input Text                      | Output |
|--------------------------------|--------|
| `Um, I’m thinking...`          | 1      |
| `um um um`                     | 3      |
| `Yummy food`                   | 0      |
| `He said, UM, loudly.`         | 1      |

---

## 🧠 How It Works

The function uses Python’s `re` module with:

```python
re.findall(r'\bum\b', s, re.IGNORECASE)
\b is a word boundary to ensure "um" is a separate word.
re.IGNORECASE makes it case-insensitive.

🧪 Testing
You can create tests in test_um.py using pytest to verify functionality.

Sample test_um.py:
from um import count

def test_single_um():
    assert count("Um, excuse me.") == 1

def test_multiple_ums():
    assert count("um um um!") == 3

def test_no_um():
    assert count("yummy umbrella") == 0

def test_case_insensitive():
    assert count("UM, um, Um.") == 3

def test_embedded_um():
    assert count("aluminum and yummy") == 0

pytest test_um.py

📝 Usage
Run the program interactively:
python um.py

Example:
Text: Um, I guess... um, sure!
2

📁 File Structure
├── um.py            # Main program
├── test_um.py       # Unit tests for count()
└── README.md        # Documentation

🧑‍💻 Author
Developed as part of CS50P, this script provides a simple use case for regular expressions and string processing.

📜 License
Free to use and modify under the MIT License.

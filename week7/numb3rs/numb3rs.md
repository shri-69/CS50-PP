# 🔢 numb3rs.py — IPv4 Address Validator

Inspired by a scene from *NUMB3RS* (Season 5, Episode 23), where a fictional IP address `275.3.6.28` is shown (which is **invalid**), this project ensures that such mistakes don’t go unnoticed.

This Python script validates whether a given string is a **valid IPv4 address**.

---

## 📜 Description

An **IPv4 address** consists of four decimal numbers (each between 0 and 255), separated by periods (e.g., `192.168.0.1`).  
The script `numb3rs.py` provides a `validate` function that returns `True` for valid IPv4 addresses and `False` otherwise.

---

## 🧠 How It Works

- Uses **regular expressions (`re`)** to match the basic structure: `#.#.#.#`
- Converts each segment into an integer and ensures:
  - No segment is less than `0` or greater than `255`
  - No non-numeric parts are allowed

---

## 🛠️ Files

### `numb3rs.py`

- Contains the `validate()` function and a `main()` function for user input.
- You can run it interactively:

```bash
python numb3rs.py

You will be prompted:
IPv4 Address: 192.168.1.1
True

# test_numb3ers.py

A test suite for the validator using pytest
Tests various categories:
✅ Valid IPs
❌ Invalid formats
❌ Out-of-range values
⚠️ IPs with leading zeros


✅ Example Valid IPs
192.168.0.1
0.0.0.0
255.255.255.255
127.0.0.1
192.168.001.001

❌ Example Invalid IPs
256.100.100.100 — 256 out of range
192.168.300.1 — 300 out of range
192.168.1 — Too few octets
192,168,1,1 — Wrong separator
999.999.999.999 — All values invalid
hello.world — Not an IP format

🧪 How to Run Tests
Make sure pytest is installed:
  pip install pytest
Then run:
  pytest test_numb3rs.py
You should see all tests passing if everything is correct.

📁 Directory Structure
├── numb3rs.py           # Main script with validate() function
├── test_numb3rs.py      # Test suite using pytest
└── README.md            # This file

👨‍💻 Author
Inspired by Harvard’s CS50, this project was created as a practice in regex, validation logic, and testing in Python.

📝 License
MIT License — feel free to use and modify for educational purposes.


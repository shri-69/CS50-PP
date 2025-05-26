# Bank 💰 – Seinfeld-Inspired Greeting Checker

This project is a fun little Python program inspired by **Season 7, Episode 24 of *Seinfeld***, where Kramer visits a bank that promises to give $100 to anyone not greeted with a "hello."

## 📝 Description

The bank's rule:
- If the greeting starts with `"hello"` → 💵 `$0`
- If it starts with `"h"` (but not `"hello"`) → 💵 `$20`
- If it starts with anything else → 💵 `$100`

This script follows those rules and gives you a simulated dollar output based on your greeting!

## 🚀 How It Works

1. Prompts the user for a greeting.
2. Strips any leading/trailing whitespace.
3. Converts the input to lowercase for case-insensitive comparison.
4. Outputs the corresponding amount of money based on the greeting.

## 🧪 Example

**Input:**
Greeting: Hello there
**Output:**
$0


**Input:**
Greeting: hey
**Output:**
$20


**Input:**
Greeting: what's up?
**Output:**
$100


## 🛠️ How to Run

Make sure Python is installed, then run the script:

```bash
python bank.py

📁 File Structure
bank.py       # Main script implementing the Seinfeld greeting logic
README.md     # Project overview and instructions


📚 Concepts Used
String methods: strip(), lower(), startswith()
Conditional statements
Input/Output

# 🚗 Vanity Plate Validator (Massachusetts DMV Rules)

This Python program validates custom (vanity) license plate entries based on the official rules provided by the Massachusetts Registry of Motor Vehicles. It determines whether a proposed plate is valid or invalid.

## 💡 Problem Description

Massachusetts allows drivers to request personalized plates, but with strict formatting rules. This program enforces those rules and ensures each plate:
- Begins with at least **two letters**
- Contains **only letters and numbers**
- Has a **length between 2 and 6 characters**, inclusive
- Has **no numbers in the middle**; numbers must come **only at the end**
- **Cannot start numbers with '0'**
- Contains **no spaces, punctuation, or special characters**

## ✅ Valid Examples

- `CS50`
- `AAA222`
- `CAR99`

## ❌ Invalid Examples

- `C50` – fewer than 2 starting letters
- `AAA22A` – number in the middle
- `AAA022` – starts number with zero
- `CS.50` – contains punctuation
- `CS 50` – contains space
- `CS50CS50` – exceeds 6 characters

## 🧠 Program Logic

The program uses the following validations:
- `len(s) < 2 or > 6` → invalid
- `s[0]` and `s[1]` must be letters
- Entire string must be alphanumeric
- Once a digit appears:
  - It must not be `0`
  - No letters can follow it

## 🧪 Example Run

Plate: CS50
Valid

Plate: AAA22A
Invalid

Plate: A1
Invalid

Plate: CS.50
Invalid


## 🗂 File Structure

- `plates.py` – Main script with:
- `main()` – Handles user input and output
- `is_valid(s)` – Validates plate according to rules

## 🧪 Optional Extension

Add `test_plates.py` to test `is_valid()` using `pytest`.

## ▶️ How to Run

Ensure Python is installed and then run:

```bash
python plates.py


📚 Learning Objectives
 - This project builds proficiency in:
 - Conditional logic
 - String manipulation
 - Iterating with enumerate()
 - Writing reusable validation functions

🏁 License
This project is inspired by CS50’s Python curriculum and is free to use for learning and educational purposes.
# 🎓 Little Professor - CS50 Python Project

`professor.py` is a Python recreation of the classic *Little Professor* toy. This educational program quizzes users with simple addition problems based on difficulty level and helps build arithmetic skills interactively.

---

## 📁 File

- `professor.py`

---

## 📝 Description

The program:

1. Prompts the user for a difficulty level:
   - `1`: Single-digit numbers (0–9)
   - `2`: Two-digit numbers (10–99)
   - `3`: Three-digit numbers (100–999)

2. Randomly generates **10 addition problems** according to the selected level.

3. Allows the user **up to 3 tries per problem**:
   - If the answer is correct, the user gets a point.
   - If the answer is incorrect, the program prints `"EEE"` and re-prompts.
   - After 3 incorrect tries, the correct answer is displayed.

4. At the end, the program displays the **user's score out of 10**.

---

## 🔢 Sample Run
Level (1, 2, or 3): 2
34 + 42 = 76
91 + 15 = 106
23 + 17 = 44
EEE
EEE
EEE
23 + 17 = 40
Score: 2


---

## ✅ Features

- Input validation for level and answers
- Tracks correct answers
- Graceful error handling with `"EEE"` messages
- Displays correct answer after 3 failed attempts

---

## 🛠️ Usage

To run the game:

```bash
python professor.py

Follow the prompt to:
- Select difficulty level (1, 2, or 3)
- Solve 10 math problems
- View your score!

📦 Dependencies
- random (standard Python library)


🧠 Educational Objective
Designed to mimic the classic Little Professor toy, this project helps reinforce:
Basic control flow
Input validation
Random number generation
Loops and error handling
Core programming concepts in Python

👨‍💻 Author
Project for CS50’s Introduction to Computer Science
by [SHRIYA DHAWAN]

📄 License
Open for learning and educational purposes.

# CS50-PP
## 🥤 Coke Machine Simulator - CS50 Problem

This Python program simulates a simple Coke vending machine. It is designed as a solution to a CS50 problem where users interact with a virtual machine that sells Coca-Cola bottles for 50 cents.

## 💡 Problem Description

The machine accepts only three coin denominations:
- 25 cents
- 10 cents
- 5 cents

The user is prompted to insert one coin at a time. After each insertion, the program displays how much is still owed. Once the total amount inserted equals or exceeds 50 cents, the program calculates and displays the change owed to the user.

Invalid coin values (i.e., coins not in the accepted denominations) are ignored.

## 🧠 Logic Used

- A `while` loop continues prompting the user until the total amount inserted reaches or exceeds 50 cents.
- Input is validated against a list of valid coin denominations.
- Change is calculated as the difference between the inserted amount and the cost.

## 📄 Files

- `coke.py`: Main program that runs the simulation.

## 🖥 Example Run
Amount Due: 50
Insert Coin: 25
Amount Due: 25
Insert Coin: 10
Amount Due: 15
Insert Coin: 10
Amount Due: 5
Insert Coin: 5
Change Owed: 0


## ✅ How to Run

Make sure you have Python installed, then in your terminal:

```bash
python coke.py

📚 Learning Outcomes
This project helps reinforce:
- Loops
- Input validation
- Conditional logic
- Basic arithmetic in Python

It’s a great exercise for beginners to practice user interaction and control flow.

🏁 License
This project is created as part of CS50 and is free to use for educational purposes.


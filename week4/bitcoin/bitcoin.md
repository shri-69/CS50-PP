# 💰 Bitcoin Price Checker – CS50 Python Project

`bitcoin.py` is a command-line tool that fetches the current price of Bitcoin from the CoinCap API and calculates the cost of purchasing a specified number of Bitcoins in real-time.

---

## 📁 File

- `bitcoin.py`

---

## 📝 Description

This program:

1. Accepts one **command-line argument**: the number of Bitcoins the user wants to buy.
2. Fetches the **current price of Bitcoin in USD** from the [CoinCap API](https://coincap.io/).
3. Calculates the **total cost** and displays it to **four decimal places**, formatted with thousands separators.
4. Handles errors for:
   - Invalid or missing input
   - API request failures
   - Unexpected API response formats

---

## 🧪 Example Usage

```bash
$ python bitcoin.py 2.5
$162,743.4575

🔐 API Authentication
- This script uses an API key from CoinCap. Make sure to:
- Register for a free CoinCap account.
- Obtain your API key.
- Replace the placeholder value in this line of bitcoin.py:
  "Authorization": "Bearer YOUR_API_KEY_HERE"


🛠️ Requirements
- Python 3
- requests module (install with pip install requests)


🧠 Educational Objectives
- This project demonstrates:
- Command-line argument parsing
- Type conversion and error handling
- Using the requests library to make HTTP requests
- Parsing JSON responses
- Formatting numerical output
- Graceful error handling and use of sys.exit()


📦 Installation
Clone or download this repository.
Install dependencies:
- pip install requests
Run the script with the desired number of Bitcoins:
- python bitcoin.py 1.5


👨‍💻 Author
Project for CS50’s Introduction to Computer Science
by [SHRIYA DHAWAN]

📄 License
This project is open for educational use.

# 🍪 Cookie Jar — A Simple Python Class

This project implements a `Jar` class to simulate a **cookie jar** that holds cookies, with support for depositing, withdrawing, and tracking cookie capacity.

---

## 📦 Features

- Initialize a cookie jar with a default or custom capacity.
- Deposit cookies into the jar.
- Withdraw cookies from the jar.
- Check the current number of cookies (`size`).
- Check the jar’s total capacity.
- Visualize the jar using emojis: `🍪🍪🍪`

---

## 🧪 Example

```python
from jar import Jar

jar = Jar(capacity=5)
print(jar)         # ""
jar.deposit(3)
print(jar)         # "🍪🍪🍪"
jar.withdraw(1)
print(jar.size)    # 2

🛑 Error Handling
Raises ValueError if:
Capacity is not a non-negative integer.
Deposit exceeds capacity.
Withdraw amount exceeds available cookies.

🧠 Methods
Method	                                            Description
__init__()	                                        Initializes the jar with optional capacity.
__str__()	                                          Returns a string of 🍪 for each cookie.
deposit(n)	                                        Adds n cookies if there's space.
withdraw(n)	                                        Removes n cookies if enough exist.
capacity	                                          Returns the jar’s max capacity.
size	                                              Returns the current cookie count.


🧪 Testing
Tests are implemented in test_jar.py.

To run the tests:
pytest test_jar.py

📁 File Structure
├── jar.py          # Jar class
├── test_jar.py     # Unit tests
└── README.md       # Project documentation

📜 License
MIT License — Free to use, learn from, and modify.


---

### ✅ `test_jar.py`

```python
import pytest
from jar import Jar

def test_default_capacity():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    assert str(jar) == ""

def test_custom_capacity():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("ten")

def test_deposit():
    jar = Jar(4)
    jar.deposit(3)
    assert jar.size == 3
    assert str(jar) == "🍪🍪🍪"

def test_deposit_overflow():
    jar = Jar(2)
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    assert str(jar) == "🍪🍪"

def test_withdraw_too_many():
    jar = Jar(3)
    jar.deposit(1)
    with pytest.raises(ValueError):
        jar.withdraw(2)

def test_str():
    jar = Jar(3)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

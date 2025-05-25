import pytest
from jar import Jar

def test_default_capacity():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_custom_capacity():
    jar = Jar(5)
    assert jar.capacity == 5

def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("ten")

def test_str_output():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit_and_overflow():
    jar = Jar(4)
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(2)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw_and_underflow():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)  

def test_empty_jar():
    jar = Jar()
    assert str(jar) == ""
    with pytest.raises(ValueError):
        jar.withdraw(1)

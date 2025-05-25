from working import convert
import pytest

def test_standard_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1:30 PM to 4:15 AM") == "13:30 to 04:15"

def test_mixed_minutes():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("11 AM to 1:00 PM") == "11:00 to 13:00"
    assert convert("12:45 PM to 3 PM") == "12:45 to 15:00"

def test_invalid_inputs():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("hello world")  

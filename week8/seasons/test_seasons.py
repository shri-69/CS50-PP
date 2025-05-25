from seasons import get_minutes_since_birth
from datetime import date, timedelta

def test_today_birth():
    today_str = date.today().strftime("%Y-%m-%d")
    assert get_minutes_since_birth(today_str) == 0

def test_yesterday_birth():
    yesterday = date.today() - timedelta(days=1)
    assert get_minutes_since_birth(yesterday.strftime("%Y-%m-%d")) == 1440

def test_20_years():
    twenty_years_ago = date.today() - timedelta(days=20*365)
    
    assert get_minutes_since_birth(twenty_years_ago.strftime("%Y-%m-%d")) == 20*365*24*60

def test_bad_format():
    try:
        get_minutes_since_birth("01-01-2000")
    except ValueError:
        assert True
    else:
        assert False

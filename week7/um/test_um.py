from um import count

def test_basic_cases():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM UM um") == 3

def test_with_punctuation():
    assert count("um, hi") == 1
    assert count("hello... um.") == 1
    assert count("Um! Did you see that?") == 1

def test_as_substrings():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0
    assert count("Umami is tasty") == 0

def test_multiple_ums_spaced_out():
    assert count("well um uh um...um") == 3
    assert count("...um... um , um") == 3

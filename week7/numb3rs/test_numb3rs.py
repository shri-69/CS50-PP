from numb3rs import validate

def test_valid_addresses():
    assert validate("0.0.0.0")
    assert validate("192.168.0.1")
    assert validate("255.255.255.255")
    assert validate("127.0.0.1")

def test_invalid_format():
    assert not validate("192.168.1")
    assert not validate("192.168.1.1.1")
    assert not validate("192,168,1,1")
    assert not validate("hello.world")

def test_out_of_range():
    assert not validate("256.100.100.100")
    assert not validate("192.168.300.1")
    assert not validate("-1.0.0.0")
    assert not validate("999.999.999.999")

def test_leading_zeros():

    assert validate("192.168.001.001")      

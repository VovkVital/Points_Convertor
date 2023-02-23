from working import convert
import pytest


def main():
    test_format()
    test_time()
    test_time_hour()

def test_format():
    with pytest.raises(ValueError):
        assert convert("9 PM - 9 AM")

def test_time():
    with pytest.raises(ValueError):
        assert convert("9:60 PM - 9:60 AM")

def test_time_hour():
    with pytest.raises(ValueError):
        assert convert("9:59 PM - 19:59 AM")

main()
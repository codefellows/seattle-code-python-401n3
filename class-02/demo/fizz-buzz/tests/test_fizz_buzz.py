from fizz_buzz import __version__
from fizz_buzz.fizz import fizz_buzz


def test_version():
    assert __version__ == '0.1.0'

def test_one():
    actual = fizz_buzz(1)
    expected = 1
    assert actual == expected

def test_one_not_two():
    actual = fizz_buzz(1)
    expected = 2
    assert actual != expected

def test_three():
    actual = fizz_buzz(3)
    expected = 'Fizz'
    assert actual == expected

def test_five():
    actual = fizz_buzz(5)
    expected = 'Buzz'
    assert actual == expected

def test_fifteen():
    actual = fizz_buzz(15)
    expected = 'FizzBuzz'
    assert actual == expected

def test_pass_in_string():
    actual = fizz_buzz('fifteen')
    expected = 15
    assert actual == expected

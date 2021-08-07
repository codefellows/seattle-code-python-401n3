from main import add, subtract

def test_add_pass():
    assert add(1, 1) == 2

def test_subtract_pass():
    assert subtract(1, 1) == 0
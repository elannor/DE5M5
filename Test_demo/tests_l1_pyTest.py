from calculator import Calculator

def test_sum():
    calculation = Calculator(8, 2)
    assert calculation.get_sum() == 10, "The sum is wrong"

def test_diff():
    calculation = Calculator(8, 2)
    assert calculation.get_diff() == 6, "The substraction is wrong"

def test_prod():
    calculation = Calculator(8, 2)
    assert calculation.get_prod() == 16, "The mult is wrong"

def test_div():
    calculation = Calculator(8, 2)
    assert calculation.get_div() == 4, "The div is wrong"
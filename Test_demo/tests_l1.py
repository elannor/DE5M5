import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):
    
    def test_sum(self):
        calculation = Calculator(8,2)
        answer = calculation.get_sum()
        self.assertEqual(answer, 10, 'The sum is wrong')

    def test_diff(self):
        calculation = Calculator(8,2)
        answer = calculation.get_diff()
        self.assertEqual(answer, 6, 'The substraction is wrong')

    def test_prod(self):
        calculation = Calculator(8,2)
        answer = calculation.get_prod()
        self.assertEqual(answer, 16, 'The mult is wrong')

    def test_div(self):
        calculation = Calculator(8,2)
        answer = calculation.get_div()
        self.assertEqual(answer, 4, 'The div is wrong')

if __name__ == "__main__":
    unittest.main()
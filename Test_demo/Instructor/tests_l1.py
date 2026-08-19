import unittest
from calculator import Calculator

class TestOperatins(unittest.TestCase):

    def test_sum(self):
        calculation = Calculator(8,2)
        answer = calculation.get_sum()
        self.assertEqual(answer, 10, "The sum is wrong.")

    # Write the remaining tests for the remaining functions. 
    def test_div(self):
        calculation = Calculator(8,2)
        answer = calculation.get_div()
        self.assertEqual(answer, 4, "The sum is wrong.")
    # Stretch: research pyTest

    
if __name__ == "__main__":
    unittest.main()
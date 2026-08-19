import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator(8,2)

    def test_sum(self):
        self.assertEqual(self.calc.get_sum(), 10, 'The sum is wrong')
   

if __name__ == "__main__":
    unittest.main()
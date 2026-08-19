import unittest
from calculator import Calculator

class TestOperatins(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator(8,2)
    
    def test_sum(self):
        self.assertEqual(self.calc.get_prod(), 16, "The sum is wrong")
    
    def tearDown(self):
        pass
    
if __name__ == "__main__":
    unittest.main()
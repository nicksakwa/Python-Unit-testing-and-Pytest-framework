import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add_positive_number(self):
        result= add(2,3)
        self.assertEqual(result, 5)
    def test_add_negative_number(self):
        result= add(-2,-3)
        self.assertEqual(result, -5)

if __name__ == '__main__':
    unittest.main()
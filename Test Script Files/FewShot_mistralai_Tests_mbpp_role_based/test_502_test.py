import unittest
from mbpp_502_code import find

class TestFind(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find(10, 3), 1)
        self.assertEqual(find(25, 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(find(-10, 3), 1)
        self.assertEqual(find(-25, 5), 1)

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, find, 0, 0)

    def test_negative_number_as_modulus(self):
        self.assertEqual(find(10, -3), 1)
        self.assertEqual(find(-25, -5), 1)

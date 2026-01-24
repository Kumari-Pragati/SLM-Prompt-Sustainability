import unittest
from mbpp_502_code import find

class TestFind(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find(10, 3), 1)

    def test_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            find(10, 0)

    def test_negative_numbers(self):
        self.assertEqual(find(-10, 3), -1)

    def test_large_numbers(self):
        self.assertEqual(find(1000000, 100), 0)

    def test_small_numbers(self):
        self.assertEqual(find(5, 2), 1)

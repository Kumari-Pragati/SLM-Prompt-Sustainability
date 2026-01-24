import unittest
from mbpp_292_code import find

class TestFind(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find(10, 2), 5)

    def test_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            find(10, 0)

    def test_negative_numbers(self):
        self.assertEqual(find(-10, 2), -5)

    def test_zero_dividend(self):
        self.assertEqual(find(0, 2), 0)

    def test_large_numbers(self):
        self.assertEqual(find(1000, 10), 100)

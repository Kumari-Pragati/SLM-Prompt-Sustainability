import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):

    def test_simple_addition(self):
        self.assertEqual(count_digits(1, 2), 3)
        self.assertEqual(count_digits(10, 20), 4)
        self.assertEqual(count_digits(100, 200), 7)

    def test_edge_cases(self):
        self.assertEqual(count_digits(0, 1), 1)
        self.assertEqual(count_digits(1, 0), 1)
        self.assertEqual(count_digits(0, 0), 1)
        self.assertEqual(count_digits(999_999_999, 999_999_999), 18)

    def test_negative_numbers(self):
        self.assertEqual(count_digits(-1, 2), 3)
        self.assertEqual(count_digits(-10, -20), 4)
        self.assertEqual(count_digits(-100, -200), 7)

    def test_special_cases(self):
        self.assertEqual(count_digits(1_000_000_000_000_000, 1), 21)
        self.assertEqual(count_digits(1, 1_000_000_000_000_000), 21)
        self.assertEqual(count_digits(1_000_000_000_000_000, 1_000_000_000_000_000), 22)

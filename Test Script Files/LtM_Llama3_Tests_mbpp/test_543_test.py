import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_digits(10, 20), 2)
        self.assertEqual(count_digits(100, 200), 3)
        self.assertEqual(count_digits(0, 0), 0)

    def test_edge(self):
        self.assertEqual(count_digits(0, 1), 1)
        self.assertEqual(count_digits(1, 0), 1)
        self.assertEqual(count_digits(0, 0), 0)

    def test_max(self):
        self.assertEqual(count_digits(999999, 999999), 6)
        self.assertEqual(count_digits(1000000, 1000000), 7)

    def test_min(self):
        self.assertEqual(count_digits(-1, -1), 2)
        self.assertEqual(count_digits(-100, -100), 3)

    def test_negative(self):
        self.assertEqual(count_digits(-10, 20), 2)
        self.assertEqual(count_digits(-100, 200), 3)

    def test_zero(self):
        self.assertEqual(count_digits(0, 0), 0)
        self.assertEqual(count_digits(0, 1), 1)

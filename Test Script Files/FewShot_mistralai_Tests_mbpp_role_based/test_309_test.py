import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):
    def test_same_numbers(self):
        self.assertEqual(maximum(5, 5), 5)

    def test_positive_numbers(self):
        self.assertEqual(maximum(2, 3), 3)
        self.assertEqual(maximum(10, 5), 10)

    def test_negative_numbers(self):
        self.assertEqual(maximum(-2, -3), -2)
        self.assertEqual(maximum(-10, -5), -5)

    def test_zero(self):
        self.assertEqual(maximum(0, 0), 0)
        self.assertEqual(maximum(0, -1), 0)
        self.assertEqual(maximum(-0, 0), 0)

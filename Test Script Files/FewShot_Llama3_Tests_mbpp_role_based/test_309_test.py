import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):
    def test_equal_numbers(self):
        self.assertEqual(maximum(5, 5), 5)

    def test_a_greater_than_b(self):
        self.assertEqual(maximum(10, 5), 10)

    def test_b_greater_than_a(self):
        self.assertEqual(maximum(5, 10), 10)

    def test_negative_numbers(self):
        self.assertEqual(maximum(-5, -10), -5)

    def test_zero(self):
        self.assertEqual(maximum(0, 0), 0)

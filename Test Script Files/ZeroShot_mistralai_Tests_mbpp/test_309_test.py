import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(maximum(5, 3), 5)
        self.assertEqual(maximum(10, 2), 10)
        self.assertEqual(maximum(1, 100), 100)

    def test_negative_numbers(self):
        self.assertEqual(maximum(-5, -3), -3)
        self.assertEqual(maximum(-10, -2), -10)
        self.assertEqual(maximum(-1, -100), -1)

    def test_zero(self):
        self.assertEqual(maximum(0, 5), 5)
        self.assertEqual(maximum(5, 0), 5)
        self.assertEqual(maximum(0, 0), 0)

    def test_floats(self):
        self.assertEqual(maximum(3.14, 2.71), 3.14)
        self.assertEqual(maximum(-3.14, -2.71), -2.71)
        self.assertEqual(maximum(0.0, 3.14), 3.14)
        self.assertEqual(maximum(3.14, 0.0), 3.14)

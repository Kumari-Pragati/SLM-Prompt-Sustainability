import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(maximum(5, 3), 5)
        self.assertEqual(maximum(10, 2), 10)
        self.assertEqual(maximum(1, 1), 1)

    def test_zero_and_positive_numbers(self):
        self.assertEqual(maximum(0, 5), 5)
        self.assertEqual(maximum(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(maximum(-3, -5), -3)
        self.assertEqual(maximum(-10, -2), -10)
        self.assertEqual(maximum(-1, -1), -1)

    def test_mixed_numbers(self):
        self.assertEqual(maximum(-3, 5), 5)
        self.assertEqual(maximum(-10, 2), 10)
        self.assertEqual(maximum(-1, 1), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, maximum, "a", 3)
        self.assertRaises(TypeError, maximum, 3, "b")

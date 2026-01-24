import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):
    def test_same_numbers(self):
        self.assertEqual(compute_Last_Digit(1, 1), 1)
        self.assertEqual(compute_Last_Digit(10, 10), 1)
        self.assertEqual(compute_Last_Digit(100, 100), 1)

    def test_different_numbers(self):
        self.assertEqual(compute_Last_Digit(1, 2), 0)
        self.assertEqual(compute_Last_Digit(10, 11), 0)
        self.assertEqual(compute_Last_Digit(100, 101), 0)

    def test_difference_greater_than_5(self):
        self.assertEqual(compute_Last_Digit(1, 6), 0)
        self.assertEqual(compute_Last_Digit(10, 15), 0)
        self.assertEqual(compute_Last_Digit(100, 105), 0)

    def test_difference_less_than_5(self):
        self.assertEqual(compute_Last_Digit(1, 2), 0)
        self.assertEqual(compute_Last_Digit(10, 11), 0)
        self.assertEqual(compute_Last_Digit(100, 101), 0)

    def test_negative_numbers(self):
        self.assertEqual(compute_Last_Digit(-1, -2), 0)
        self.assertEqual(compute_Last_Digit(-10, -11), 0)
        self.assertEqual(compute_Last_Digit(-100, -101), 0)

    def test_zero(self):
        self.assertEqual(compute_Last_Digit(0, 0), 1)

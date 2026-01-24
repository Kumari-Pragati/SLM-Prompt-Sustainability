import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):

    def test_same_numbers(self):
        self.assertEqual(compute_Last_Digit(5, 5), 1)

    def test_different_numbers_with_difference_greater_than_5(self):
        self.assertEqual(compute_Last_Digit(5, 10), 0)
        self.assertEqual(compute_Last_Digit(10, 15), 0)

    def test_different_numbers_with_difference_less_than_5(self):
        self.assertEqual(compute_Last_Digit(5, 6), 1)
        self.assertEqual(compute_Last_Digit(6, 5), 1)
        self.assertEqual(compute_Last_Digit(1, 2), 1)
        self.assertEqual(compute_Last_Digit(2, 1), 2)

    def test_zero_and_positive_numbers(self):
        self.assertEqual(compute_Last_Digit(0, 5), 5)
        self.assertEqual(compute_Last_Digit(5, 0), 5)

    def test_negative_numbers(self):
        self.assertEqual(compute_Last_Digit(-5, -3), 5)
        self.assertEqual(compute_Last_Digit(-3, -5), 3)

    def test_large_numbers(self):
        self.assertEqual(compute_Last_Digit(1000000, 1000001), 1)
        self.assertEqual(compute_Last_Digit(1000001, 1000000), 1)

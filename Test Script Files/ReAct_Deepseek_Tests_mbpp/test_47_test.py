import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):

    def test_same_numbers(self):
        self.assertEqual(compute_Last_Digit(5, 5), 1)

    def test_difference_greater_than_five(self):
        self.assertEqual(compute_Last_Digit(1, 7), 0)

    def test_difference_less_than_five(self):
        self.assertEqual(compute_Last_Digit(3, 6), 36)

    def test_negative_numbers(self):
        self.assertEqual(compute_Last_Digit(-3, -6), 36)

    def test_zero_as_input(self):
        self.assertEqual(compute_Last_Digit(0, 10), 0)

    def test_large_numbers(self):
        self.assertEqual(compute_Last_Digit(100, 105), 1)

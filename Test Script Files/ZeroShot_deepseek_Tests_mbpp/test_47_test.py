import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):

    def test_same_numbers(self):
        self.assertEqual(compute_Last_Digit(5, 5), 1)
        self.assertEqual(compute_Last_Digit(0, 0), 1)

    def test_difference_greater_than_five(self):
        self.assertEqual(compute_Last_Digit(6, 10), 0)
        self.assertEqual(compute_Last_Digit(15, 20), 0)

    def test_difference_less_than_five(self):
        self.assertEqual(compute_Last_Digit(3, 7), 6)
        self.assertEqual(compute_Last_Digit(1, 5), 1)

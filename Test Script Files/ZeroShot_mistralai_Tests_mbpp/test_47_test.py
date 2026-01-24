import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):

    def test_same_numbers(self):
        self.assertEqual(compute_Last_Digit(5, 5), 1)

    def test_different_numbers_with_difference_greater_than_5(self):
        self.assertEqual(compute_Last_Digit(5, 10), 0)

    def test_different_numbers_with_difference_less_than_5(self):
        self.assertEqual(compute_Last_Digit(5, 7), 5)

    def test_edge_cases(self):
        self.assertEqual(compute_Last_Digit(0, 5), 5)
        self.assertEqual(compute_Last_Digit(5, 0), 5)
        self.assertEqual(compute_Last_Digit(1, 2), 1)
        self.assertEqual(compute_Last_Digit(2, 1), 2)

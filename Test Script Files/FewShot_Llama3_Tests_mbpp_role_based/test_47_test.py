import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):
    def test_same_numbers(self):
        self.assertEqual(compute_Last_Digit(10, 10), 1)

    def test_large_difference(self):
        self.assertEqual(compute_Last_Digit(10, 15), 0)

    def test_small_difference(self):
        self.assertEqual(compute_Last_Digit(10, 12), 4)

    def test_edge_case_A_equals_B_plus_one(self):
        self.assertEqual(compute_Last_Digit(10, 11), 1)

    def test_edge_case_A_equals_B_minus_one(self):
        self.assertEqual(compute_Last_Digit(10, 9), 1)

    def test_edge_case_A_equals_B(self):
        self.assertEqual(compute_Last_Digit(10, 10), 1)

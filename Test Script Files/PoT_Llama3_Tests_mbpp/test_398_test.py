import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_of_digits([123, 456, 789]), 27)

    def test_edge_case_single_digit(self):
        self.assertEqual(sum_of_digits([1, 2, 3]), 6)

    def test_edge_case_zero(self):
        self.assertEqual(sum_of_digits([0, 1, 2]), 3)

    def test_edge_case_negative(self):
        self.assertEqual(sum_of_digits([-1, -2, -3]), -6)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_of_digits([]), 0)

    def test_edge_case_single_zero(self):
        self.assertEqual(sum_of_digits([0]), 0)

    def test_edge_case_single_negative(self):
        self.assertEqual(sum_of_digits([-1]), -1)

    def test_edge_case_single_negative_zero(self):
        self.assertEqual(sum_of_digits([-1, 0]), -1)

    def test_edge_case_single_negative_zero_list(self):
        self.assertEqual(sum_of_digits([-1, 0, 1]), 0)

    def test_edge_case_single_negative_zero_list_with_negative(self):
        self.assertEqual(sum_of_digits([-1, 0, -1]), -2)

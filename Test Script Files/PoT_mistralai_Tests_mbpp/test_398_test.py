import unittest
from mbpp_398_code import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_of_digits([123, 456, 789]), 21)

    def test_edge_case_zero(self):
        self.assertEqual(sum_of_digits([0]), 0)

    def test_edge_case_negative(self):
        self.assertEqual(sum_of_digits([-123, -456, -789]), 12)

    def test_edge_case_single_digit(self):
        self.assertEqual(sum_of_digits([1]), 1)

    def test_edge_case_multi_digit_single_number(self):
        self.assertEqual(sum_of_digits([12345]), 15)

    def test_corner_case_empty_list(self):
        self.assertEqual(sum_of_digits([]), 0)

    def test_corner_case_non_integer(self):
        self.assertEqual(sum_of_digits(['a', 'b', 'c']), 0)

import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):

    def test_simple_case(self):
        self.assertListEqual(divisible_by_digits(12, 20), [12, 13, 14, 15, 16, 17, 18, 19])

    def test_edge_case_min(self):
        self.assertListEqual(divisible_by_digits(0, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_max(self):
        self.assertListEqual(divisible_by_digits(1000000000, 1000000009), [])

    def test_edge_case_single_digit(self):
        self.assertListEqual(divisible_by_digits(1, 1), [1])

    def test_edge_case_zero(self):
        self.assertListEqual(divisible_by_digits(0, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_special_flags(self):
        self.assertListEqual(divisible_by_digits(10, 10), [])
        self.assertListEqual(divisible_by_digits(100, 100), [])
        self.assertListEqual(divisible_by_digits(1000, 1000), [])

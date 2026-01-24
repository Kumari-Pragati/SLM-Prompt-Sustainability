import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(divisible_by_digits(12345, 56789), [12348, 12350, 12351, 12352, 12353, 12354, 12355, 12356, 12357, 12359, 56788, 56789])

    def test_edge_case_start(self):
        self.assertListEqual(divisible_by_digits(0, 12345), [])

    def test_edge_case_end(self):
        self.assertListEqual(divisible_by_digits(12345, 0), [])

    def test_edge_case_single_digit(self):
        self.assertListEqual(divisible_by_digits(1, 10), [1])

    def test_edge_case_all_zeroes(self):
        self.assertListEqual(divisible_by_digits(0, 0), [])

    def test_edge_case_all_nines(self):
        self.assertListEqual(divisible_by_digits(999999999, 9999999999), [999999999])

    def test_corner_case_empty_string(self):
        self.assertListEqual(divisible_by_digits(0, 0), [])

    def test_corner_case_non_numeric(self):
        self.assertListEqual(divisible_by_digits('abc', 123), [])

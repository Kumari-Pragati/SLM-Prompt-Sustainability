import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 12, 14, 15, 18, 20])

    def test_single_digit_numbers(self):
        self.assertEqual(divisible_by_digits(1, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_startnum_greater_than_endnum(self):
        self.assertEqual(divisible_by_digits(20, 10), [])

    def test_edge_case_startnum_equals_endnum(self):
        self.assertEqual(divisible_by_digits(10, 10), [10])

    def test_edge_case_startnum_equals_0(self):
        self.assertEqual(divisible_by_digits(0, 10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_edge_case_endnum_equals_0(self):
        self.assertEqual(divisible_by_digits(10, 0), [])

    def test_edge_case_startnum_less_than_0(self):
        self.assertEqual(divisible_by_digits(-10, 10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_edge_case_endnum_greater_than_10000(self):
        self.assertEqual(divisible_by_digits(10000, 10050), [10000, 10002, 10004, 10005, 10008, 10010])

    def test_edge_case_startnum_less_than_minus10000(self):
        self.assertEqual(divisible_by_digits(-10050, -10000), [])

    def test_edge_case_startnum_equals_minus10000_and_endnum_equals_10000(self):
        self.assertEqual(divisible_by_digits(-10000, 10000), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_startnum_equals_minus10000_and_endnum_equals_minus9999(self):
        self.assertEqual(divisible_by_digits(-10000, -9999), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_startnum_equals_minus9999_and_endnum_equals_10000(self):
        self.assertEqual(divisible_by_digits(-9999, 10000), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_startnum_equals_minus9999_and_endnum_equals_minus10000(self):
        self.assertEqual(divisible_by_digits(-9999, -10000), [])

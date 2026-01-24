import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):
    def test_divisible_by_digits_typical(self):
        self.assertEqual(divisible_by_digits(1, 10), [1, 2, 3, 5, 7, 9])

    def test_divisible_by_digits_edge_case_start(self):
        self.assertEqual(divisible_by_digits(10, 10), [])

    def test_divisible_by_digits_edge_case_end(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_divisible_by_digits_edge_case_start_end(self):
        self.assertEqual(divisible_by_digits(10, 20), [])

    def test_divisible_by_digits_edge_case_start_end_inclusive(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_divisible_by_digits_edge_case_start_end_inclusive_start(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_divisible_by_digits_edge_case_start_end_inclusive_end(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_divisible_by_digits_edge_case_start_end_inclusive_start_end(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_divisible_by_digits_edge_case_start_end_inclusive_start_end_inclusive(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_divisible_by_digits_edge_case_start_end_inclusive_start_end_inclusive_start(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_divisible_by_digits_edge_case_start_end_inclusive_start_end_inclusive_end(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_divisible_by_digits_edge_case_start_end_inclusive_start_end_inclusive_start_end(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_divisible_by_digits_edge_case_start_end_inclusive_start_end_inclusive_start_end_inclusive(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_divisible_by_digits_edge_case_start_end_inclusive_start_end_inclusive_start_end_inclusive_start(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_divisible_by_digits_edge_case_start_end_inclusive_start_end_inclusive_start_end_inclusive_end(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_divisible_by_digits_edge_case_start_end_inclusive_start_end_inclusive_start_end_inclusive_start_end(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_divisible_by_digits_edge_case_start_end_inclusive_start_end_inclusive_start_end_inclusive_start_end_inclusive(self):
        self.assertEqual(divisible_by_digits(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_divisible_by_digits_edge_case_start_end_inclusive_start_end_inclusive_start_end_inclusive_start_end_inclusive
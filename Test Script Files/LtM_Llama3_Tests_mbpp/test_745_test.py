import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(divisible_by_digits(1, 10), [1, 2, 3, 5, 7, 9])

    def test_edge_case_start_zero(self):
        self.assertEqual(divisible_by_digits(0, 10), [])

    def test_edge_case_end_zero(self):
        self.assertEqual(divisible_by_digits(1, 0), [])

    def test_edge_case_start_end_equal(self):
        self.assertEqual(divisible_by_digits(5, 5), [5])

    def test_edge_case_start_end_equal_with_zero(self):
        self.assertEqual(divisible_by_digits(0, 0), [])

    def test_edge_case_start_end_equal_with_negative(self):
        self.assertEqual(divisible_by_digits(-5, -5), [])

    def test_edge_case_start_end_equal_with_negative_zero(self):
        self.assertEqual(divisible_by_digits(-5, -5), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive(self):
        self.assertEqual(divisible_by_digits(-5, 5), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero(self):
        self.assertEqual(divisible_by_digits(-5, 0), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative(self):
        self.assertEqual(divisible_by_digits(-5, -5), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero(self):
        self.assertEqual(divisible_by_digits(-5, 0), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero_and_negative(self):
        self.assertEqual(divisible_by_digits(-5, -5), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero_and_negative_and_positive(self):
        self.assertEqual(divisible_by_digits(-5, 5), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero_and_negative_and_positive_with_zero(self):
        self.assertEqual(divisible_by_digits(-5, 0), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero_and_negative_and_positive_with_zero_and_negative(self):
        self.assertEqual(divisible_by_digits(-5, -5), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero_and_negative_and_positive_with_zero_and_negative_and_positive(self):
        self.assertEqual(divisible_by_digits(-5, 5), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero(self):
        self.assertEqual(divisible_by_digits(-5, 0), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero_and_negative(self):
        self.assertEqual(divisible_by_digits(-5, -5), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero_and_negative_and_positive(self):
        self.assertEqual(divisible_by_digits(-5, 5), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero_and_negative(self):
        self.assertEqual(divisible_by_digits(-5, -5), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero_and_negative_and_positive(self):
        self.assertEqual(divisible_by_digits(-5, 5), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero_and_negative_and_positive(self):
        self.assertEqual(divisible_by_digits(-5, -5), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero_and_negative_and_positive(self):
        self.assertEqual(divisible_by_digits(-5, 5), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero_and_negative_and_positive(self):
        self.assertEqual(divisible_by_digits(-5, -5), [])

    def test_edge_case_start_end_equal_with_negative_zero_and_positive_with_zero_and_negative_and_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero_and_negative_and_positive_with_zero_and_negative_and_positive(self):
        self.assertEqual(divisible_by_digits(-5
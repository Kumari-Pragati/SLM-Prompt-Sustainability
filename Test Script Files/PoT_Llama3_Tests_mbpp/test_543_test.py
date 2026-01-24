import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_digits(123, 456), 3)

    def test_edge_case_zero(self):
        self.assertEqual(count_digits(0, 0), 0)

    def test_edge_case_single_digit(self):
        self.assertEqual(count_digits(1, 2), 1)

    def test_edge_case_large_numbers(self):
        self.assertEqual(count_digits(123456, 789012), 6)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(count_digits(-123, 456), 3)

    def test_edge_case_mixed_signs(self):
        self.assertEqual(count_digits(-123, 456), 3)

    def test_edge_case_zero_with_non_zero(self):
        self.assertEqual(count_digits(0, 123), 2)

    def test_edge_case_non_zero_with_zero(self):
        self.assertEqual(count_digits(123, 0), 3)

    def test_edge_case_large_negative_numbers(self):
        self.assertEqual(count_digits(-123456, -789012), 6)

    def test_edge_case_mixed_signs_large(self):
        self.assertEqual(count_digits(-123456, 789012), 6)

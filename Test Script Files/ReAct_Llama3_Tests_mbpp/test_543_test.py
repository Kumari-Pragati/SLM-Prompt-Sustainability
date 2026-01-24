import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(count_digits(0,0), 0)

    def test_single_digit(self):
        self.assertEqual(count_digits(1,0), 1)

    def test_multiple_digits(self):
        self.assertEqual(count_digits(123,456), 3)

    def test_negative_numbers(self):
        self.assertEqual(count_digits(-123,456), 3)

    def test_mixed_signs(self):
        self.assertEqual(count_digits(-123,456), 3)

    def test_zero_in_second_position(self):
        self.assertEqual(count_digits(0,123), 3)

    def test_zero_in_first_position(self):
        self.assertEqual(count_digits(0,0), 1)

    def test_edge_case_zero(self):
        self.assertEqual(count_digits(0,0), 1)

    def test_edge_case_single_digit(self):
        self.assertEqual(count_digits(1,0), 1)

    def test_edge_case_zero_in_first_position(self):
        self.assertEqual(count_digits(0,0), 1)

    def test_edge_case_zero_in_second_position(self):
        self.assertEqual(count_digits(0,0), 1)

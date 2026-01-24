import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_Digit(0), 0)

    def test_single_digit(self):
        self.assertEqual(count_Digit(123), 3)

    def test_multiple_digits(self):
        self.assertEqual(count_Digit(123456), 6)

    def test_negative_number(self):
        self.assertEqual(count_Digit(-123), 3)

    def test_zero_with_leading_zeros(self):
        self.assertEqual(count_Digit(0000), 4)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            count_Digit('123')

    def test_edge_case_zero_with_leading_zeros(self):
        self.assertEqual(count_Digit(000), 3)

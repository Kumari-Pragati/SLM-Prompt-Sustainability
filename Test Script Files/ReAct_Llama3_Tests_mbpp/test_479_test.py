import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_Digit(12345), 1)

    def test_edge_case_zero(self):
        self.assertEqual(first_Digit(0), 0)

    def test_edge_case_single_digit(self):
        self.assertEqual(first_Digit(1), 1)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            first_Digit(-12345)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            first_Digit('12345')

    def test_edge_case_large_number(self):
        self.assertEqual(first_Digit(123456789), 1)

    def test_edge_case_large_negative_number(self):
        with self.assertRaises(OverflowError):
            first_Digit(-1234567890123456789)

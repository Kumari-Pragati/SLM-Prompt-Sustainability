import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_Digit(123), 1)

    def test_edge_case_zero(self):
        self.assertEqual(first_Digit(0), 0)

    def test_edge_case_single_digit(self):
        self.assertEqual(first_Digit(5), 5)

    def test_edge_case_negative(self):
        self.assertEqual(first_Digit(-123), 1)

    def test_edge_case_negative_zero(self):
        self.assertEqual(first_Digit(-0), 0)

    def test_edge_case_negative_single_digit(self):
        self.assertEqual(first_Digit(-5), -5)

    def test_edge_case_large_number(self):
        self.assertEqual(first_Digit(123456789), 1)

    def test_edge_case_large_negative_number(self):
        self.assertEqual(first_Digit(-123456789), -1)

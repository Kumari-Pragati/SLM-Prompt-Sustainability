import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(last_Digit(123), 3)

    def test_edge_case_zero(self):
        self.assertEqual(last_Digit(0), 0)

    def test_edge_case_negative(self):
        self.assertEqual(last_Digit(-123), 3)

    def test_edge_case_large_number(self):
        self.assertEqual(last_Digit(123456789), 9)

    def test_edge_case_large_negative_number(self):
        self.assertEqual(last_Digit(-123456789), 9)

    def test_edge_case_large_positive_number(self):
        self.assertEqual(last_Digit(1234567890), 0)

    def test_edge_case_large_negative_number_with_zero(self):
        self.assertEqual(last_Digit(-1234567890), 0)

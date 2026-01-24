import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(decimal_to_Octal(10), 12)

    def test_edge_case_zero(self):
        self.assertEqual(decimal_to_Octal(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(decimal_to_Octal(1), 1)

    def test_edge_case_max(self):
        self.assertEqual(decimal_to_Octal(255), 377)

    def test_edge_case_min(self):
        self.assertEqual(decimal_to_Octal(-1), -1)

    def test_edge_case_negative(self):
        self.assertEqual(decimal_to_Octal(-10), -12)

    def test_edge_case_max_negative(self):
        self.assertEqual(decimal_to_Octal(-255), -377)

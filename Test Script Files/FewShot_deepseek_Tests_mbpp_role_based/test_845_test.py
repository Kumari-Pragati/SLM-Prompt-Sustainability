import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_Digits(1234), 4)

    def test_edge_condition(self):
        self.assertEqual(find_Digits(0), 1)

    def test_boundary_condition(self):
        self.assertEqual(find_Digits(10**18), 19)

    def test_negative_number(self):
        self.assertEqual(find_Digits(-1), 0)

    def test_single_digit_number(self):
        self.assertEqual(find_Digits(5), 1)

    def test_large_number(self):
        self.assertEqual(find_Digits(10**10), 11)

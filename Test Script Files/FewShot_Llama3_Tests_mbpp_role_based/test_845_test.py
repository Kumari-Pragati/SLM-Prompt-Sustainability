import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(find_Digits(10), 2)

    def test_negative_integer(self):
        self.assertEqual(find_Digits(-10), 0)

    def test_zero(self):
        self.assertEqual(find_Digits(0), 1)

    def test_one(self):
        self.assertEqual(find_Digits(1), 1)

    def test_large_integer(self):
        self.assertEqual(find_Digits(1000), 4)

    def test_edge_case(self):
        self.assertEqual(find_Digits(10**100), 101)

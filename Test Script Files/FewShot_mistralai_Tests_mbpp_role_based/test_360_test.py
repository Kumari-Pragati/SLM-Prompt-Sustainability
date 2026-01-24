import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(get_carol(1), 3)
        self.assertEqual(get_carol(2), 31)
        self.assertEqual(get_carol(3), 783)

    def test_zero(self):
        self.assertEqual(get_carol(0), 1)

    def test_negative_numbers(self):
        self.assertEqual(get_carol(-1), -3)
        self.assertEqual(get_carol(-2), -31)
        self.assertEqual(get_carol(-3), -783)

    def test_large_numbers(self):
        self.assertEqual(get_carol(10), 1023)
        self.assertEqual(get_carol(20), 1048573)
        self.assertEqual(get_carol(30), 1073741823)

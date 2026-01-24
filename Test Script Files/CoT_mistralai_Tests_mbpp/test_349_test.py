import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(check(""), "No")

    def test_single_digit(self):
        self.assertEqual(check("0"), "Yes")
        self.assertEqual(check("1"), "Yes")

    def test_multiple_digits(self):
        self.assertEqual(check("00"), "Yes")
        self.assertEqual(check("11"), "Yes")
        self.assertEqual(check("01"), "No")
        self.assertEqual(check("10"), "No")

    def test_mixed_digits(self):
        self.assertEqual(check("010"), "No")
        self.assertEqual(check("101"), "No")
        self.assertEqual(check("011"), "No")
        self.assertEqual(check("100"), "No")

    def test_string_with_non_digits(self):
        self.assertEqual(check("0a"), "No")
        self.assertEqual(check("1b"), "No")
        self.assertEqual(check("01a"), "No")
        self.assertEqual(check("10b"), "No")

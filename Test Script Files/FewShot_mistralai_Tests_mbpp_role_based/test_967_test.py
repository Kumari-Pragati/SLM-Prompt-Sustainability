import unittest
from mbpp_967_code import check

class TestCheck(unittest.TestCase):
    def test_accepted_long_string(self):
        self.assertEqual(check("aeiouaeiou"), "accepted")

    def test_accepted_short_string(self):
        self.assertEqual(check("AeIoU"), "accepted")

    def test_accepted_mixed_case(self):
        self.assertEqual(check("aEiOu"), "accepted")

    def test_not_accepted_short_string(self):
        self.assertEqual(check("A"), "not accepted")

    def test_not_accepted_long_string_with_non_vowels(self):
        self.assertEqual(check("abcdefghijklmnopqrstuvwxyz"), "not accepted")

import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(number_of_substrings("abc"), 11)
        self.assertEqual(number_of_substrings("a"), 1)
        self.assertEqual(number_of_substrings("aa"), 2)
        self.assertEqual(number_of_substrings("aaaa"), 6)
        self.assertEqual(number_of_substrings("abab"), 11)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(number_of_substrings(""), 0)
        self.assertEqual(number_of_substrings("1234567890"), 45)
        self.assertEqual(number_of_substrings("01234567890"), 46)
        self.assertEqual(number_of_substrings("12345678901"), 47)

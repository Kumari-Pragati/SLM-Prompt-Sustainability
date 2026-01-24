import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(number_of_substrings("a"), 1)
        self.assertEqual(number_of_substrings("ab"), 3)
        self.assertEqual(number_of_substrings("abc"), 6)

    def test_edge_conditions(self):
        self.assertEqual(number_of_substrings(""), 0)
        self.assertEqual(number_of_substrings(" "), 1)

    def test_complex_cases(self):
        self.assertEqual(number_of_substrings("abcd"), 10)
        self.assertEqual(number_of_substrings("12345"), 15)
        self.assertEqual(number_of_substrings("abcdefghijklmnopqrstuvwxyz"), 515)

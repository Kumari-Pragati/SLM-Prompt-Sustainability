import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(number_of_substrings("abc"), 11)

    def test_edge_input(self):
        self.assertEqual(number_of_substrings(""), 0)
        self.assertEqual(number_of_substrings("a" * 1000), 500000)

    def test_boundary_input(self):
        self.assertEqual(number_of_substrings("a" * 10), 55)
        self.assertEqual(number_of_substrings("a" * 20), 221)

    def test_complex_input(self):
        self.assertEqual(number_of_substrings("abab"), 10)
        self.assertEqual(number_of_substrings("aabbcc"), 21)

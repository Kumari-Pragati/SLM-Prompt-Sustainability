import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):

    def test_string_length_normal(self):
        self.assertEqual(string_length("hello"), 5)
        self.assertEqual(string_length(""), 0)
        self.assertEqual(string_length("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_string_length_edge_cases(self):
        self.assertEqual(string_length("a" * 10000), 10000)
        self.assertEqual(string_length("A" * 10000), 10000)
        self.assertEqual(string_length("!" * 10000), 10000)
        self.assertEqual(string_length("0123456789" * 10000), 10000)

    def test_string_length_special_cases(self):
        self.assertEqual(string_length("\n"), 1)
        self.assertEqual(string_length("\t"), 1)
        self.assertEqual(string_length("\r"), 1)
        self.assertEqual(string_length("\u200b"), 1)

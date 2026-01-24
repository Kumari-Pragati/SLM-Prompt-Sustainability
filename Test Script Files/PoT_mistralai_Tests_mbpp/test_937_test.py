import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_char("hello"), "l")
        self.assertEqual(max_char("Python"), "o")
        self.assertEqual(max_char("Test"), "t")

    def test_edge_case_empty_string(self):
        self.assertEqual(max_char(""), "")

    def test_edge_case_single_char(self):
        self.assertEqual(max_char("a"), "a")

    def test_edge_case_all_same_char(self):
        self.assertEqual(max_char("aaaaa"), "a")

    def test_edge_case_no_uppercase(self):
        self.assertEqual(max_char("abcdefghijklmnopqrstuvwxyz"), "z")

    def test_edge_case_no_lowercase(self):
        self.assertEqual(max_char("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "Z")

    def test_edge_case_mixed_case(self):
        self.assertEqual(max_char("AbCdEfGhIjKlMnOpQrStUvWxYz"), "z")
        self.assertEqual(max_char("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"), "Z")

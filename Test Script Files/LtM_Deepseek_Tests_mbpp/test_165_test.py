import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_char_position("ABC"), 3)
        self.assertEqual(count_char_position("abc"), 3)
        self.assertEqual(count_char_position("Abc"), 3)
        self.assertEqual(count_char_position("AbC"), 3)

    def test_edge_conditions(self):
        self.assertEqual(count_char_position(""), 0)
        self.assertEqual(count_char_position("A"), 1)
        self.assertEqual(count_char_position("a"), 1)
        self.assertEqual(count_char_position("123"), 0)
        self.assertEqual(count_char_position("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)
        self.assertEqual(count_char_position("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_complex_cases(self):
        self.assertEqual(count_char_position("AbCdEfGhIjKlMnOpQrStUvWxYz"), 52)
        self.assertEqual(count_char_position("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"), 52)
        self.assertEqual(count_char_position("AaBbCc"), 6)
        self.assertEqual(count_char_position("1a2B3c"), 1)

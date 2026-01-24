import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_long_word("Hello world"), ["Hello"])

    def test_edge_case(self):
        self.assertEqual(find_long_word("a"), [])
        self.assertEqual(find_long_word("123456"), ["12345"])

    def test_corner_case(self):
        self.assertEqual(find_long_word("abcdefghijklmnopqrstuvwxyz"), ["abcdefghijklmnopqrstuvwxy"])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_long_word(123)
        with self.assertRaises(TypeError):
            find_long_word(None)

import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sort_String("hello"), "ehllo")

    def test_empty(self):
        self.assertEqual(sort_String(""), "")

    def test_single_char(self):
        self.assertEqual(sort_String("a"), "a")

    def test_all_same_chars(self):
        self.assertEqual(sort_String("aaa"), "aaa")

    def test_mixed_chars(self):
        self.assertEqual(sort_String("abc"), "abc")

    def test_repeated_chars(self):
        self.assertEqual(sort_String("aabbc"), "aabbc")

    def test_long_string(self):
        self.assertEqual(sort_String("abcdefghijklmnopqrstuvwxyz"), "abcdefghijklmnopqrstuvwxyz")

    def test_punctuation(self):
        self.assertEqual(sort_String("Hello, World!"), ",HdeWlo!r")

    def test_numbers(self):
        self.assertEqual(sort_String("123abc"), "123abc")

    def test_spaces(self):
        self.assertEqual(sort_String("   hello   "), "   ehlllo   ")

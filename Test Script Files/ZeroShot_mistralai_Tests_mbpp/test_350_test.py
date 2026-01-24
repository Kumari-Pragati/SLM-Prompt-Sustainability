import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(minimum_Length(""), 0)

    def test_single_character(self):
        self.assertEqual(minimum_Length("a"), 0)
        self.assertEqual(minimum_Length("z"), 0)

    def test_single_character_repeated(self):
        self.assertEqual(minimum_Length("aa"), 1)
        self.assertEqual(minimum_Length("zz"), 1)

    def test_multiple_characters(self):
        self.assertEqual(minimum_Length("abcd"), 0)
        self.assertEqual(minimum_Length("abcde"), 1)
        self.assertEqual(minimum_Length("abcdefg"), 2)

    def test_multiple_characters_repeated(self):
        self.assertEqual(minimum_Length("aaaaa"), 1)
        self.assertEqual(minimum_Length("zzzzz"), 1)
        self.assertEqual(minimum_Length("aaaaazz"), 2)

    def test_long_string(self):
        self.assertEqual(minimum_Length("abcdefghijklmnopqrstuvwxyz"), 26)

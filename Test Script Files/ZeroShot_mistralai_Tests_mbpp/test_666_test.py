import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_char("", "a"), 0)

    def test_single_char_string(self):
        self.assertEqual(count_char("a", "a"), 1)
        self.assertEqual(count_char("A", "a"), 0)

    def test_multiple_chars_string(self):
        self.assertEqual(count_char("aaa", "a"), 3)
        self.assertEqual(count_char("AAA", "A"), 3)

    def test_mixed_case_string(self):
        self.assertEqual(count_char("Aa1Bb2Cc3", "a"), 1)
        self.assertEqual(count_char("Aa1Bb2Cc3", "A"), 1)

    def test_special_chars(self):
        self.assertEqual(count_char("!@#$%^&*()_+-=", "$"), 3)

    def test_non_existent_char(self):
        self.assertEqual(count_char("abc", "d"), 0)

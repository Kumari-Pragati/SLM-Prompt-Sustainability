import unittest
from mbpp_30_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_two_characters_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ab"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("aa"), 3)

    def test_multiple_characters_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 3)
        self.assertEqual(count_Substring_With_Equal_Ends("aab"), 4)
        self.assertEqual(count_Substring_With_Equal_Ends("aaa"), 7)

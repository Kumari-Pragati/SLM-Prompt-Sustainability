import unittest
from mbpp_338_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(''), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends('a'), 1)

    def test_multiple_characters_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends('abc'), 3)
        self.assertEqual(count_Substring_With_Equal_Ends('aab'), 2)
        self.assertEqual(count_Substring_With_Equal_Ends('aaa'), 6)

    def test_string_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends('abca'), 3)
        self.assertEqual(count_Substring_With_Equal_Ends('abcba'), 6)
        self.assertEqual(count_Substring_With_Equal_Ends('aabbaa'), 10)

    def test_string_without_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends('abcd'), 3)
        self.assertEqual(count_Substring_With_Equal_Ends('abcde'), 4)
        self.assertEqual(count_Substring_With_Equal_Ends('abcdef'), 5)

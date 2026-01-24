import unittest
from mbpp_338_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abccba"), 10)

    def test_single_character(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_all_same_characters(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aaaaa"), 15)

    def test_no_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcde"), 0)

    def test_large_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcdefg"*1000), 4995000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Substring_With_Equal_Ends(123)

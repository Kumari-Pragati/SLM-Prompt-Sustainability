import unittest

from mbpp_30_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcab"), 2)

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_all_same_characters(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aaaaa"), 15)

    def test_all_different_characters(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 0)

    def test_boundary_case(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"*30), 465)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Substring_With_Equal_Ends(123)

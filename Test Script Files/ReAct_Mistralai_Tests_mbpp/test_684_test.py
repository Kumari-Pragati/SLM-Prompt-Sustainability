import unittest
from mbpp_684_code import count_Char

class TestCountChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Char("", "a"), 0)

    def test_single_character(self):
        self.assertEqual(count_Char("a", "a"), 1)

    def test_multiple_characters(self):
        self.assertEqual(count_Char("abcdef", "a"), 4)

    def test_case_sensitivity(self):
        self.assertEqual(count_Char("ABC", "C"), 3)

    def test_single_character_in_long_string(self):
        self.assertEqual(count_Char("xyzabcxyz", "a"), 2)

    def test_long_string_with_single_character_at_end(self):
        self.assertEqual(count_Char("xyzabc", "z"), 1)

    def test_long_string_with_single_character_at_beginning(self):
        self.assertEqual(count_Char("zabc", "z"), 1)

    def test_long_string_with_single_character_in_middle(self):
        self.assertEqual(count_Char("xyzabc", "b"), 1)

    def test_string_with_only_one_occurrence(self):
        self.assertEqual(count_Char("abc", "c"), 1)

    def test_string_with_multiple_occurrences(self):
        self.assertEqual(count_Char("aaa", "a"), 3)

    def test_string_with_no_occurrences(self):
        self.assertEqual(count_Char("xyz", "a"), 0)

    def test_negative_string_length(self):
        with self.assertRaises(ValueError):
            count_Char("abc", -1)

    def test_empty_character(self):
        with self.assertRaises(ValueError):
            count_Char("abc", "")

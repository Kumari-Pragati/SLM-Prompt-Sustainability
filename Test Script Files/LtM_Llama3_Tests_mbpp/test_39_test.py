import unittest
from mbpp_39_code import rearange_string

class TestRearangeString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(rearange_string(""), "")

    def test_single_char_string(self):
        self.assertEqual(rearange_string("a"), "a")

    def test_two_char_string(self):
        self.assertEqual(rearange_string("ab"), "ab")

    def test_three_char_string(self):
        self.assertEqual(rearange_string("abc"), "abc")

    def test_four_char_string(self):
        self.assertEqual(rearange_string("abcd"), "abcd")

    def test_five_char_string(self):
        self.assertEqual(rearange_string("abcde"), "abcde")

    def test_string_with_duplicates(self):
        self.assertEqual(rearange_string("aabbcc"), "aabbc")

    def test_string_with_duplicates_and_gaps(self):
        self.assertEqual(rearange_string("aabbccdd"), "aabbcdd")

    def test_string_with_duplicates_and_gaps_and_spaces(self):
        self.assertEqual(rearange_string("aabbccdd ee"), "aabbcdd ee")

    def test_string_with_duplicates_and_gaps_and_spaces_and_punctuation(self):
        self.assertEqual(rearange_string("aabbccdd ee.,"), "aabbcdd ee.,")

    def test_string_with_duplicates_and_gaps_and_spaces_and_punctuation_and_numbers(self):
        self.assertEqual(rearange_string("aabbccdd ee.,123"), "aabbcdd ee.,123")

    def test_string_with_duplicates_and_gaps_and_spaces_and_punctuation_and_numbers_and_special_chars(self):
        self.assertEqual(rearange_string("aabbccdd ee.,123!@#"), "aabbcdd ee.,123!@#")

    def test_string_with_duplicates_and_gaps_and_spaces_and_punctuation_and_numbers_and_special_chars_and_newlines(self):
        self.assertEqual(rearange_string("aabbccdd ee.,123!@# \n"), "aabbcdd ee.,123!@# \n")

    def test_string_with_duplicates_and_gaps_and_spaces_and_punctuation_and_numbers_and_special_chars_and_newlines_and_tabs(self):
        self.assertEqual(rearange_string("aabbccdd ee.,123!@# \n\t"), "aabbcdd ee.,123!@# \n\t")

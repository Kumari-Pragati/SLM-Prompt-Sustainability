import unittest
from mbpp_39_code import rearange_string

class TestRearangeString(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(rearange_string("aabbc"), "abcba")

    def test_edge_case_empty_string(self):
        self.assertEqual(rearange_string(""), "")

    def test_edge_case_single_character_string(self):
        self.assertEqual(rearange_string("a"), "a")

    def test_edge_case_single_character_string_with_duplicates(self):
        self.assertEqual(rearange_string("aa"), "aa")

    def test_edge_case_single_character_string_with_duplicates_and_spaces(self):
        self.assertEqual(rearange_string("a a"), "a a")

    def test_edge_case_single_character_string_with_duplicates_and_spaces_and_punctuation(self):
        self.assertEqual(rearange_string("a, a"), "a, a")

    def test_edge_case_single_character_string_with_duplicates_and_spaces_and_punctuation_and_numbers(self):
        self.assertEqual(rearange_string("a, a1"), "a, a1")

    def test_edge_case_single_character_string_with_duplicates_and_spaces_and_punctuation_and_numbers_and_special_characters(self):
        self.assertEqual(rearange_string("a, a1!"), "a, a1!")

    def test_edge_case_single_character_string_with_duplicates_and_spaces_and_punctuation_and_numbers_and_special_characters_and_uppercase(self):
        self.assertEqual(rearange_string("A, a1!"), "A, a1!")

    def test_edge_case_single_character_string_with_duplicates_and_spaces_and_punctuation_and_numbers_and_special_characters_and_uppercase_and_lowercase(self):
        self.assertEqual(rearange_string("A, a1!a"), "A, a1!a")

    def test_edge_case_single_character_string_with_duplicates_and_spaces_and_punctuation_and_numbers_and_special_characters_and_uppercase_and_lowercase_and_punctuation(self):
        self.assertEqual(rearange_string("A, a1!a,."), "A, a1!a,")

    def test_edge_case_single_character_string_with_duplicates_and_spaces_and_punctuation_and_numbers_and_special_characters_and_uppercase_and_lowercase_and_punctuation_and_spaces(self):
        self.assertEqual(rearange_string("A, a1!a,,"), "A, a1!a,,")

    def test_edge_case_single_character_string_with_duplicates_and_spaces_and_punctuation_and_numbers_and_special_characters_and_uppercase_and_lowercase_and_punctuation_and_spaces_and_numbers(self):
        self.assertEqual(rearange_string("A, a1!a,,1"), "A, a1!a,,1")

    def test_edge_case_single_character_string_with_duplicates_and_spaces_and_punctuation_and_numbers_and_special_characters_and_uppercase_and_lowercase_and_punctuation_and_spaces_and_numbers_and_punctuation(self):
        self.assertEqual(rearange_string("A, a1!a,,1!"), "A, a1!a,,1!")

    def test_edge_case_single_character_string_with_duplicates_and_spaces_and_punctuation_and_numbers_and_special_characters_and_uppercase_and_lowercase_and_punctuation_and_spaces_and_numbers_and_punctuation_and_uppercase(self):
        self.assertEqual(rearange_string("A, a1!a,,1!A"), "A, a1!a,,1!A")

    def test_edge_case_single_character_string_with_duplicates_and_spaces_and_punctuation_and_numbers_and_special_characters_and_uppercase_and_lowercase_and_punctuation_and_spaces_and_numbers_and_punctuation_and_uppercase_and_lowercase(self):
        self.assertEqual(rearange_string("A, a1!a,,1!A, a"), "A, a1!a,,1!A, a")

    def test_edge_case_single_character_string_with_duplicates_and_spaces_and_punctuation_and_numbers_and_special_characters_and_uppercase_and_lowercase_and_punctuation_and_spaces_and_numbers_and_punctuation_and_uppercase_and_lowercase_and_punctuation(self):
        self.assertEqual(rearange_string("A, a1!a,,1!A, a,."), "A, a1!a,,1!A, a,")

    def test_edge_case_single_character_string_with_duplicates_and_spaces_and_punctuation_and_numbers_and_special_characters_and_uppercase_and_lowercase_and_punctuation_and_spaces_and_numbers_and_punctuation_and_uppercase_and_lowercase_and_punctuation_and_spaces(self):
        self.assertEqual(rearange_string("A, a1!a,,1!A, a,,"), "A, a1!a,,1!A, a,,")

    def test_edge_case_single_character_string_with_duplicates_and_spaces_and_punctuation_and_numbers_and_special_characters_and_uppercase_and_lowercase_and_punctuation_and_spaces_and_numbers_and_punctuation_and_uppercase_and_lowercase_and_punctuation_and_spaces_and_numbers(self):
        self.assertEqual(rearange_string("A, a1!a,,1!A, a,,1"), "A, a1!a,,1!A, a,,1")

    def
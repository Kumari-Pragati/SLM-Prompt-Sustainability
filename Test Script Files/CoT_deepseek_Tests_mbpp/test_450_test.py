import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_string(["abc", "defg", "hijk", "lmno"], 3), ["abc", "hijk"])

    def test_empty_string(self):
        self.assertEqual(extract_string([], 3), [])

    def test_string_with_length_l(self):
        self.assertEqual(extract_string(["abcdefg"], 3), ["abcdefg"])

    def test_string_with_length_greater_than_l(self):
        self.assertEqual(extract_string(["abcdefg"], 4), [])

    def test_string_with_multiple_length_l(self):
        self.assertEqual(extract_string(["abc", "defg", "hijk", "lmno"], 3), ["abc", "hijk"])

    def test_string_with_mixed_lengths(self):
        self.assertEqual(extract_string(["abc", "defg", "hijk", "lmno"], 2), ["defg"])

    def test_string_with_special_characters(self):
        self.assertEqual(extract_string(["abc!", "defg", "hijk", "lmno"], 3), ["abc!"])

    def test_string_with_numbers(self):
        self.assertEqual(extract_string(["abc123", "defg", "hijk", "lmno"], 3), ["abc123"])

    def test_string_with_spaces(self):
        self.assertEqual(extract_string(["abc def", "hijk", "lmno"], 3), ["abc def"])

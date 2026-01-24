import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):

    def test_common_prefix_empty_list(self):
        self.assertEqual(common_prefix([], 0), "")

    def test_common_prefix_single_element_list(self):
        self.assertEqual(common_prefix(["abc"], 1), "abc")

    def test_common_prefix_single_element_list_case_insensitive(self):
        self.assertEqual(common_prefix(["AbC"], 1), "AbC")

    def test_common_prefix_two_elements(self):
        self.assertEqual(common_prefix(["abc", "abcd"], 2), "abc")

    def test_common_prefix_two_elements_case_insensitive(self):
        self.assertEqual(common_prefix(["AbC", "AbCD"], 2), "AbC")

    def test_common_prefix_different_lengths(self):
        self.assertEqual(common_prefix(["abc", "ab"], 2), "ab")

    def test_common_prefix_empty_strings(self):
        self.assertEqual(common_prefix(["", "def"], 2), "")

    def test_common_prefix_only_spaces(self):
        self.assertEqual(common_prefix(["   ", "   "], 2), "   ")

    def test_common_prefix_special_characters(self):
        self.assertEqual(common_prefix(["123", "1234"], 2), "123")

    def test_common_prefix_invalid_input_empty_string(self):
        with self.assertRaises(ValueError):
            common_prefix(["abc", "def"], 0)

    def test_common_prefix_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            common_prefix([1, 2, 3], 3)

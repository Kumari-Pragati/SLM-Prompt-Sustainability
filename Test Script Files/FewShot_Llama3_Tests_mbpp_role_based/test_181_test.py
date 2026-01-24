import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):
    def test_common_prefix_with_single_element_array(self):
        self.assertEqual(common_prefix(["hello"], 1), "hello")

    def test_common_prefix_with_multiple_elements_array(self):
        self.assertEqual(common_prefix(["hello", "hello world", "hello again"], 3), "hello")

    def test_common_prefix_with_empty_array(self):
        with self.assertRaises(IndexError):
            common_prefix([], 1)

    def test_common_prefix_with_array_of_empty_strings(self):
        self.assertEqual(common_prefix(["", "", ""], 3), "")

    def test_common_prefix_with_array_of_strings_of_different_lengths(self):
        self.assertEqual(common_prefix(["abc", "abcd", "abcde"], 3), "abc")

    def test_common_prefix_with_array_of_strings_with_spaces(self):
        self.assertEqual(common_prefix(["hello world", "hello again", "hello there"], 3), "hello")

    def test_common_prefix_with_array_of_strings_with_special_characters(self):
        self.assertEqual(common_prefix(["hello!", "hello?", "hello!"], 3), "hello")

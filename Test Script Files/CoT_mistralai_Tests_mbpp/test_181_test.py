import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(common_prefix([], 0), "")

    def test_single_element_list(self):
        self.assertEqual(common_prefix([ "abc" ], 1), "abc")

    def test_identical_strings(self):
        self.assertEqual(common_prefix(["abc", "abc"], 2), "abc")

    def test_different_lengths(self):
        self.assertEqual(common_prefix(["abc", "ab"], 2), "ab")

    def test_empty_strings(self):
        self.assertEqual(common_prefix(["", "def"], 2), "")

    def test_case_sensitivity(self):
        self.assertEqual(common_prefix(["AbC", "abc"], 2), "AbC")

    def test_single_char_strings(self):
        self.assertEqual(common_prefix(["a", "b"], 2), "")

    def test_invalid_input(self):
        self.assertRaises(TypeError, common_prefix, [1, 2], 2)
        self.assertRaises(TypeError, common_prefix, ["abc", 2], 1)

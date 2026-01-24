import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(common_prefix([], 0))

    def test_single_element_list(self):
        self.assertEqual(common_prefix([ "abc" ], 1), "abc")

    def test_identical_strings(self):
        self.assertEqual(common_prefix(["abc", "abc"], 2), "abc")

    def test_different_lengths(self):
        self.assertEqual(common_prefix(["abc", "ab"], 2), "ab")

    def test_different_strings(self):
        self.assertEqual(common_prefix(["abc", "def"], 2), "")

    def test_mixed_case(self):
        self.assertEqual(common_prefix(["AbC", "abc"], 2), "ab")

    def test_empty_strings(self):
        self.assertEqual(common_prefix(["", "abc"], 2), "")

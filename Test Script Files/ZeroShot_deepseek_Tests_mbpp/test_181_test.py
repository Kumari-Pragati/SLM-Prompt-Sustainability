import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):

    def test_common_prefix_util(self):
        self.assertEqual(common_prefix_util("abcdef", "abc"), "abc")
        self.assertEqual(common_prefix_util("abc", "abcdef"), "abc")
        self.assertEqual(common_prefix_util("abc", "def"), "")
        self.assertEqual(common_prefix_util("", "abc"), "")
        self.assertEqual(common_prefix_util("", ""), "")

    def test_common_prefix(self):
        self.assertEqual(common_prefix(["abcdef", "abc", "abcde"], 3), "abc")
        self.assertEqual(common_prefix(["abc", "abcdef", "def"], 3), "")
        self.assertEqual(common_prefix(["abc", "def"], 2), "")
        self.assertEqual(common_prefix(["", "abc"], 2), "")
        self.assertEqual(common_prefix(["", ""], 2), "")

import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):

    def test_common_prefix(self):
        self.assertEqual(common_prefix(["hello", "hello world", "hello again"], 3), "hello")
        self.assertEqual(common_prefix(["abc", "abcd", "abce"], 3), "abc")
        self.assertEqual(common_prefix(["a", "ab", "abc"], 3), "abc")
        self.assertEqual(common_prefix(["a", "b", "c"], 1), "a")
        self.assertEqual(common_prefix(["", "abc", "def"], 3), "")
        self.assertEqual(common_prefix(["", "abc", "def"], 1), "")

    def test_common_prefix_empty(self):
        self.assertEqual(common_prefix([], 0), "")
        self.assertEqual(common_prefix([""], 1), "")

    def test_common_prefix_single_element(self):
        self.assertEqual(common_prefix(["abc"], 1), "abc")
        self.assertEqual(common_prefix([""], 1), "")

    def test_common_prefix_all_empty(self):
        self.assertEqual(common_prefix(["", "", ""], 3), "")

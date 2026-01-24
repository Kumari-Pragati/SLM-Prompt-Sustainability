import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):
    def test_common_prefix(self):
        self.assertEqual(common_prefix(["abc", "abcd", "abce"], 3), "abc")
        self.assertEqual(common_prefix(["hello", "hello world", "hello again"], 3), "hello")
        self.assertEqual(common_prefix(["", "abc", "abcd", "abce"], 3), "")
        self.assertEqual(common_prefix(["", "abc", "abcd", "abce"], 1), "")
        self.assertEqual(common_prefix(["", "abc", "abcd", "abce"], 0), "")

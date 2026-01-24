import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(IndexError, common_prefix, [], 0)

    def test_single_element_list(self):
        self.assertEqual(common_prefix([b"abc"], 1), b"abc")
        self.assertEqual(common_prefix([b"a"], 1), b"a")
        self.assertEqual(common_prefix([b""], 1), b"")

    def test_identical_strings(self):
        self.assertEqual(common_prefix([b"abc", b"abc"], 2), b"abc")
        self.assertEqual(common_prefix([b"a", b"aa"], 2), b"a")
        self.assertEqual(common_prefix([b"123", b"1234"], 2), b"123")

    def test_non_identical_strings(self):
        self.assertEqual(common_prefix([b"abc", b"def"], 2), b"")
        self.assertEqual(common_prefix([b"a", b"b"], 2), b"")
        self.assertEqual(common_prefix([b"123", b"456"], 2), b"")

    def test_mixed_case_strings(self):
        self.assertEqual(common_prefix([b"AbC", b"abC"], 2), b"AbC")
        self.assertEqual(common_prefix([b"aBc", b"AbC"], 2), b"aBc")
        self.assertEqual(common_prefix([b"123", b"1234"], 2), b"123")

    def test_empty_strings(self):
        self.assertEqual(common_prefix([b"", b"abc"], 2), b"")
        self.assertEqual(common_prefix([b"abc", b""], 2), b"")
        self.assertEqual(common_prefix([b"", b""], 2), b"")

import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):
    def test_simple_concat(self):
        self.assertTrue(check_Concat("abc", "abc"))
        self.assertTrue(check_Concat("abc", "def"))
        self.assertTrue(check_Concat("abc", "abcabc"))

    def test_edge_concat(self):
        self.assertFalse(check_Concat("a", "b"))
        self.assertFalse(check_Concat("abc", ""))
        self.assertFalse(check_Concat("", "abc"))

    def test_concat_with_repeats(self):
        self.assertTrue(check_Concat("abcabc", "abc"))
        self.assertTrue(check_Concat("abcabc", "def"))
        self.assertTrue(check_Concat("abcabc", "abcabc"))

    def test_concat_with_empty_strings(self):
        self.assertFalse(check_Concat("", ""))
        self.assertFalse(check_Concat("abc", ""))

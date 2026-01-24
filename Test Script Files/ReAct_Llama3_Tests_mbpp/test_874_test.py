import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):

    def test_true_concat(self):
        self.assertTrue(check_Concat("abcabc", "abc"))

    def test_false_concat(self):
        self.assertFalse(check_Concat("abcd", "abc"))

    def test_concat_length_divisible(self):
        self.assertTrue(check_Concat("abcdef", "abc"))

    def test_concat_length_not_divisible(self):
        self.assertFalse(check_Concat("abcdef", "abcd"))

    def test_concat_empty(self):
        self.assertTrue(check_Concat("", ""))

    def test_concat_single_char(self):
        self.assertTrue(check_Concat("a", "a"))

    def test_concat_empty_str1(self):
        self.assertFalse(check_Concat("", "abc"))

    def test_concat_empty_str2(self):
        self.assertTrue(check_Concat("abc", ""))

    def test_concat_same_str(self):
        self.assertTrue(check_Concat("abcabc", "abcabc"))

    def test_concat_diff_str(self):
        self.assertFalse(check_Concat("abcabc", "defdef"))

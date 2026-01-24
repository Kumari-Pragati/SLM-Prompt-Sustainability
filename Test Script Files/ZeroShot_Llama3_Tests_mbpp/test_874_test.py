import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):

    def test_check_concat_true(self):
        self.assertTrue(check_Concat("abcabc", "abc"))

    def test_check_concat_false(self):
        self.assertFalse(check_Concat("abcd", "abc"))

    def test_check_concat_false2(self):
        self.assertFalse(check_Concat("abc", "def"))

    def test_check_concat_true2(self):
        self.assertTrue(check_Concat("abcdefabcdef", "abc"))

    def test_check_concat_false3(self):
        self.assertFalse(check_Concat("abcdefabcdef", "def"))

    def test_check_concat_true3(self):
        self.assertTrue(check_Concat("abcabcabc", "abc"))

    def test_check_concat_false4(self):
        self.assertFalse(check_Concat("abcabcabc", "def"))

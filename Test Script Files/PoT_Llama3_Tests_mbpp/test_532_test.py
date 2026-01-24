import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_permutation("abc", "cab"))

    def test_edge_case_equal(self):
        self.assertTrue(check_permutation("abc", "abc"))

    def test_edge_case_empty(self):
        self.assertTrue(check_permutation("", ""))

    def test_edge_case_single_char(self):
        self.assertTrue(check_permutation("a", "a"))

    def test_edge_case_single_char_empty(self):
        self.assertTrue(check_permutation("a", ""))

    def test_edge_case_empty_single_char(self):
        self.assertTrue(check_permutation("", "a"))

    def test_edge_case_empty_single_char_empty(self):
        self.assertTrue(check_permutation("", ""))

    def test_edge_case_diff_len(self):
        self.assertFalse(check_permutation("abc", "abcd"))

    def test_edge_case_diff_len_empty(self):
        self.assertFalse(check_permutation("abc", ""))

    def test_edge_case_diff_len_empty(self):
        self.assertFalse(check_permutation("", "abc"))

    def test_edge_case_diff_len_empty_empty(self):
        self.assertTrue(check_permutation("", ""))

    def test_edge_case_diff_len_single_char(self):
        self.assertFalse(check_permutation("a", "ab"))

    def test_edge_case_diff_len_single_char_empty(self):
        self.assertFalse(check_permutation("a", ""))

    def test_edge_case_diff_len_empty_single_char(self):
        self.assertFalse(check_permutation("", "a"))

    def test_edge_case_diff_len_empty_single_char_empty(self):
        self.assertTrue(check_permutation("", ""))

import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_undulating("123456789"))

    def test_edge_case1(self):
        self.assertFalse(is_undulating("12"))

    def test_edge_case2(self):
        self.assertFalse(is_undulating("123"))

    def test_edge_case3(self):
        self.assertTrue(is_undulating("123456789012"))

    def test_edge_case4(self):
        self.assertFalse(is_undulating("123456789012345"))

    def test_edge_case5(self):
        self.assertFalse(is_undulating(""))

    def test_edge_case6(self):
        self.assertFalse(is_undulating("a"))

    def test_edge_case7(self):
        self.assertFalse(is_undulating("abc"))

    def test_edge_case8(self):
        self.assertTrue(is_undulating("abcabcabc"))

    def test_edge_case9(self):
        self.assertFalse(is_undulating("abcabcabcabc"))

    def test_edge_case10(self):
        self.assertFalse(is_undulating("abcabcabcabcabc"))

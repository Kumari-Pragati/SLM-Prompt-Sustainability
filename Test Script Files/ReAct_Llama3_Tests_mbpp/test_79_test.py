import unittest
from mbpp_79_code import word_len

class TestWordLen(unittest.TestCase):

    def test_typical_case(self):
        self.assertFalse(word_len("hello world"))

    def test_edge_case1(self):
        self.assertTrue(word_len("hello"))

    def test_edge_case2(self):
        self.assertTrue(word_len("hello world hello"))

    def test_edge_case3(self):
        self.assertFalse(word_len("hello world hello world"))

    def test_edge_case4(self):
        self.assertFalse(word_len(""))

    def test_edge_case5(self):
        self.assertFalse(word_len("hello world "))

    def test_edge_case6(self):
        self.assertFalse(word_len("hello world hello world "))

    def test_edge_case7(self):
        self.assertFalse(word_len("hello world hello world hello"))

    def test_edge_case8(self):
        self.assertFalse(word_len("hello world hello world hello world"))

    def test_edge_case9(self):
        self.assertFalse(word_len("hello world hello world hello world hello"))

    def test_edge_case10(self):
        self.assertFalse(word_len("hello world hello world hello world hello world"))

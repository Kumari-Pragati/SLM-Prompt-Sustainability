import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(end_num("hello123"))

    def test_edge_case1(self):
        self.assertTrue(end_num("hello"))

    def test_edge_case2(self):
        self.assertTrue(end_num("123hello"))

    def test_edge_case3(self):
        self.assertFalse(end_num("hello"))

    def test_edge_case4(self):
        self.assertFalse(end_num("123"))

    def test_edge_case5(self):
        self.assertTrue(end_num("123456"))

    def test_edge_case6(self):
        self.assertFalse(end_num("abcdef"))

    def test_edge_case7(self):
        self.assertFalse(end_num(""))

    def test_edge_case8(self):
        self.assertFalse(end_num("1234567890"))

    def test_edge_case9(self):
        self.assertFalse(end_num("abcdefg"))

    def test_edge_case10(self):
        self.assertFalse(end_num("123456789012345678901234567890"))

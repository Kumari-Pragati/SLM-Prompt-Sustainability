import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(chkList([1, 1, 1]))

    def test_edge_case(self):
        self.assertTrue(chkList([1]))

    def test_edge_case2(self):
        self.assertTrue(chkList([1, 1]))

    def test_edge_case3(self):
        self.assertFalse(chkList([1, 2]))

    def test_edge_case4(self):
        self.assertFalse(chkList([1, 1, 2]))

    def test_edge_case5(self):
        self.assertFalse(chkList([1, 2, 3]))

    def test_edge_case6(self):
        self.assertFalse(chkList([1, 1, 1, 2]))

    def test_edge_case7(self):
        self.assertFalse(chkList([1, 1, 1, 1, 2]))

    def test_edge_case8(self):
        self.assertFalse(chkList([1, 1, 1, 1, 1, 2]))

    def test_edge_case9(self):
        self.assertFalse(chkList([1, 1, 1, 1, 1, 1, 2]))

    def test_edge_case10(self):
        self.assertFalse(chkList([1, 1, 1, 1, 1, 1, 1, 2]))

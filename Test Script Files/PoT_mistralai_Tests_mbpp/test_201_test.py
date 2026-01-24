import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(chkList([1, 1, 1]))
        self.assertTrue(chkList([-1, -1, -1]))
        self.assertTrue(chkList([3.14, 3.14, 3.14]))

    def test_edge_case_single_element(self):
        self.assertTrue(chkList([1]))
        self.assertTrue(chkList([-1]))
        self.assertTrue(chkList([3.14]))

    def test_edge_case_empty_list(self):
        self.assertFalse(chkList([]))

    def test_corner_case_duplicate_types(self):
        self.assertFalse(chkList([1, '1']))
        self.assertFalse(chkList([1, 1.0]))

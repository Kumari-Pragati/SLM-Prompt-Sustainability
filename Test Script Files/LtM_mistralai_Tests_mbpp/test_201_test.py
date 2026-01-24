import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):

    def test_simple_single_element(self):
        self.assertTrue(chkList([1]))

    def test_simple_multiple_elements(self):
        self.assertFalse(chkList([1, 2]))

    def test_edge_single_element_list(self):
        self.assertTrue(chkList([None]))

    def test_edge_empty_list(self):
        self.assertTrue(chkList([]))

    def test_edge_single_element_tuple(self):
        self.assertTrue(chkList((1,)))

    def test_edge_empty_tuple(self):
        self.assertTrue(chkList(()))

    def test_complex_single_element_set(self):
        self.assertTrue(chkList(set([1])))

    def test_complex_single_element_dict(self):
        self.assertTrue(chkList({1: 1}))

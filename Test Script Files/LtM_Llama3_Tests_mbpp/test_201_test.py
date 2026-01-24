import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):
    def test_single_element_list(self):
        self.assertTrue(chkList([1]))
    def test_single_element_tuple(self):
        self.assertTrue(chkList((1,)))
    def test_empty_list(self):
        self.assertFalse(chkList([]))
    def test_single_element_list_with_duplicates(self):
        self.assertTrue(chkList([1, 1, 1]))
    def test_list_with_multiple_elements(self):
        self.assertFalse(chkList([1, 2, 3]))
    def test_list_with_duplicates(self):
        self.assertFalse(chkList([1, 1, 2, 2, 3, 3]))

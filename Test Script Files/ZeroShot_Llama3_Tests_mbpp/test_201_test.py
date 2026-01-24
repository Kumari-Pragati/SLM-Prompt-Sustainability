import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(chkList([]))

    def test_single_element_list(self):
        self.assertTrue(chkList([1]))

    def test_all_elements_equal_list(self):
        self.assertTrue(chkList([1, 1, 1]))

    def test_all_elements_not_equal_list(self):
        self.assertFalse(chkList([1, 2, 3]))

    def test_list_with_duplicates(self):
        self.assertTrue(chkList([1, 1, 1, 1]))

    def test_list_with_duplicates_and_non_duplicates(self):
        self.assertFalse(chkList([1, 1, 2, 3]))

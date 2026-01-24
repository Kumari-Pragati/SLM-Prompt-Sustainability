import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):
    def test_single_element_list(self):
        self.assertTrue(chkList([1]))

    def test_all_duplicates_list(self):
        self.assertTrue(chkList([1, 1, 1, 1]))

    def test_no_duplicates_list(self):
        self.assertFalse(chkList([1, 2, 3]))

    def test_empty_list(self):
        self.assertTrue(chkList([]))

    def test_single_element_list_with_duplicates(self):
        self.assertTrue(chkList([1, 1, 1]))

    def test_list_with_no_duplicates_and_duplicates(self):
        self.assertFalse(chkList([1, 2, 3, 1]))

    def test_list_with_duplicates_and_no_duplicates(self):
        self.assertFalse(chkList([1, 1, 2]))

    def test_list_with_duplicates_and_duplicates(self):
        self.assertTrue(chkList([1, 1, 1]))

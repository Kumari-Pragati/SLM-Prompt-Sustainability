import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):

    def test_single_element_list(self):
        self.assertTrue(chkList([1]))

    def test_all_elements_equal(self):
        self.assertTrue(chkList([1, 1, 1]))

    def test_all_elements_distinct(self):
        self.assertFalse(chkList([1, 2, 3]))

    def test_empty_list(self):
        self.assertTrue(chkList([]))

    def test_list_with_duplicates(self):
        self.assertTrue(chkList([1, 1, 1, 1]))

    def test_list_with_no_duplicates(self):
        self.assertFalse(chkList([1, 2, 3, 4]))

    def test_list_with_one_duplicate(self):
        self.assertTrue(chkList([1, 2, 2]))

    def test_list_with_no_duplicates_and_length_greater_than_one(self):
        self.assertFalse(chkList([1, 2, 3]))

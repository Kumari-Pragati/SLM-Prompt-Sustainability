import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):

    def test_single_element(self):
        self.assertTrue(chkList([1]))

    def test_multiple_same_elements(self):
        self.assertTrue(chkList([1, 1, 1]))

    def test_multiple_different_elements(self):
        self.assertFalse(chkList([1, 2, 3]))

    def test_empty_list(self):
        self.assertFalse(chkList([]))

    def test_single_empty_list_element(self):
        self.assertTrue(chkList([[]]))

    def test_list_of_lists(self):
        self.assertFalse(chkList([[1], [2], [3]]))

    def test_list_with_none(self):
        self.assertFalse(chkList([None]))

    def test_list_with_floats(self):
        self.assertFalse(chkList([1.0, 2.0, 3.0]))

    def test_list_with_strings(self):
        self.assertFalse(chkList(["a", "b", "c"]))

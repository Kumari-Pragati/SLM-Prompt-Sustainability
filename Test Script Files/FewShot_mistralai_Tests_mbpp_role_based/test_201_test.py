import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):
    def test_single_element_list(self):
        self.assertTrue(chkList([1]))

    def test_empty_list(self):
        self.assertFalse(chkList([]))

    def test_multiple_elements_list(self):
        self.assertFalse(chkList([1, 2, 3]))

    def test_list_with_duplicates(self):
        self.assertTrue(chkList([1, 1, 2]))

    def test_list_with_mixed_types(self):
        self.assertFalse(chkList([1, "a", 2]))

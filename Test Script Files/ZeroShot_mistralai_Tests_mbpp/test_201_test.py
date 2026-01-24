import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(chkList([]))

    def test_single_element_list(self):
        self.assertTrue(chkList([1]))
        self.assertTrue(chkList(["a"]))
        self.assertTrue(chkList([True]))

    def test_multiple_elements_list(self):
        self.assertFalse(chkList([1, 2, 3]))
        self.assertFalse(chkList(["a", "b", "c"]))
        self.assertFalse(chkList([True, False, True]))

    def test_mixed_type_list(self):
        self.assertFalse(chkList([1, "a", True]))
        self.assertFalse(chkList(["a", 1, True]))
        self.assertFalse(chkList([True, 1, "a"]))

import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):

    def test_same_elements(self):
        self.assertTrue(chkList([1, 1, 1, 1]))
        self.assertTrue(chkList(['a', 'a', 'a', 'a']))
        self.assertTrue(chkList([True, True, True, True]))

    def test_different_elements(self):
        self.assertFalse(chkList([1, 2, 3, 4]))
        self.assertFalse(chkList(['a', 'b', 'c', 'd']))
        self.assertFalse(chkList([True, False, True, False]))

    def test_empty_list(self):
        self.assertTrue(chkList([]))

    def test_single_element(self):
        self.assertTrue(chkList([1]))
        self.assertTrue(chkList(['a']))
        self.assertTrue(chkList([True]))

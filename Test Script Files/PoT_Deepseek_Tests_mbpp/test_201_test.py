import unittest
from mbpp_201_code import chkList

class TestChkList(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(chkList([1, 1, 1]))

    def test_empty_list(self):
        self.assertTrue(chkList([]))

    def test_single_element(self):
        self.assertTrue(chkList([5]))

    def test_different_elements(self):
        self.assertFalse(chkList([1, 2, 3]))

    def test_negative_numbers(self):
        self.assertTrue(chkList([-1, -1, -1]))

    def test_mixed_numbers(self):
        self.assertTrue(chkList([1, 1, -1]))

    def test_mixed_types(self):
        self.assertFalse(chkList([1, '1', 1]))

    def test_none_elements(self):
        self.assertFalse(chkList([None, None, None]))

    def test_mixed_types_and_none(self):
        self.assertFalse(chkList([1, None, '1']))

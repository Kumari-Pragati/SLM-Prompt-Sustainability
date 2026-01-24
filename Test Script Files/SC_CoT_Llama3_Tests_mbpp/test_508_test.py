import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):

    def test_same_order(self):
        self.assertTrue(same_order([1, 2, 3], [2, 3, 1]))
        self.assertFalse(same_order([1, 2, 3], [2, 3, 4]))
        self.assertTrue(same_order([1, 2, 3, 2], [2, 3, 2, 1]))
        self.assertFalse(same_order([1, 2, 3, 4], [3, 4, 1, 2]))
        self.assertTrue(same_order([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
        self.assertFalse(same_order([1, 2, 3, 4, 5], [5, 4, 3, 2, 6]))
        self.assertTrue(same_order([1, 2, 3, 4, 5, 5], [5, 4, 3, 2, 1, 5]))
        self.assertFalse(same_order([1, 2, 3, 4, 5, 5], [5, 4, 3, 2, 6, 5]))

    def test_empty_lists(self):
        self.assertTrue(same_order([], []))
        self.assertFalse(same_order([], [1]))
        self.assertFalse(same_order([1], []))

    def test_single_element_lists(self):
        self.assertTrue(same_order([1], [1]))
        self.assertFalse(same_order([1], [2]))
        self.assertFalse(same_order([2], [1]))

    def test_lists_with_duplicates(self):
        self.assertTrue(same_order([1, 2, 2, 3], [2, 2, 3, 1]))
        self.assertFalse(same_order([1, 2, 2, 3], [2, 2, 3, 4]))

    def test_lists_with_duplicates_and_empty(self):
        self.assertTrue(same_order([1, 2, 2, 3, 3], [2, 2, 3, 3, 1]))
        self.assertFalse(same_order([1, 2, 2, 3, 3], [2, 2, 3, 4, 5]))

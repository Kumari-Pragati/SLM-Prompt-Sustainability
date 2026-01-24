import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):

    def test_empty_lists(self):
        self.assertTrue(same_order([], []))

    def test_single_element_lists(self):
        self.assertTrue(same_order([1], [1]))
        self.assertFalse(same_order([1], [2]))

    def test_identical_lists(self):
        self.assertTrue(same_order([1, 2, 3], [1, 2, 3]))

    def test_lists_with_common_elements(self):
        self.assertTrue(same_order([1, 2, 3, 4], [4, 1, 2, 3]))

    def test_lists_with_different_orders(self):
        self.assertFalse(same_order([1, 2, 3], [3, 1, 2]))

    def test_lists_with_unique_elements(self):
        self.assertFalse(same_order([1, 2, 3], [4, 5, 6]))

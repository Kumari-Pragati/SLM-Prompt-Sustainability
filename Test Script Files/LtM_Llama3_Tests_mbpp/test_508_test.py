import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):
    def test_empty_lists(self):
        self.assertTrue(same_order([], []))
    def test_single_element_lists(self):
        self.assertTrue(same_order([1], [1]))
        self.assertFalse(same_order([1], [2]))
    def test_common_elements(self):
        self.assertTrue(same_order([1, 2, 3], [2, 3, 1]))
        self.assertFalse(same_order([1, 2, 3], [2, 3, 4]))
    def test_duplicates(self):
        self.assertTrue(same_order([1, 1, 2, 2], [1, 2, 2, 1]))
    def test_order_matters(self):
        self.assertFalse(same_order([1, 2, 3], [3, 2, 1]))
    def test_lists_of_different_lengths(self):
        self.assertFalse(same_order([1, 2, 3], [1, 2]))
    def test_lists_with_duplicates_and_order_matters(self):
        self.assertFalse(same_order([1, 1, 2, 2, 3], [1, 2, 2, 3, 1]))

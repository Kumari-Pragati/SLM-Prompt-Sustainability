import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):

    def test_same_order_identical_lists(self):
        self.assertTrue(same_order([1, 2, 3], [1, 2, 3]))

    def test_same_order_common_elements(self):
        self.assertTrue(same_order([1, 2, 3, 4], [4, 1, 2, 3]))

    def test_same_order_empty_lists(self):
        self.assertTrue(same_order([], []))

    def test_same_order_no_common_elements(self):
        self.assertFalse(same_order([1, 2, 3], [4, 5, 6]))

    def test_same_order_different_orders_same_elements(self):
        self.assertTrue(same_order([2, 1, 3], [1, 2, 3]))

    def test_same_order_one_list_empty(self):
        self.assertFalse(same_order([], [1, 2, 3]))

    def test_same_order_one_list_single_element(self):
        self.assertTrue(same_order([1], [1]))

    def test_same_order_one_list_multiple_elements(self):
        self.assertTrue(same_order([1, 2], [1, 2]))

    def test_same_order_one_list_duplicate_elements(self):
        self.assertTrue(same_order([1, 1, 2], [1, 2, 1]))

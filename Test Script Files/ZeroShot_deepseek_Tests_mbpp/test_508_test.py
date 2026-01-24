import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):

    def test_same_order_same_elements(self):
        self.assertTrue(same_order([1, 2, 3], [1, 2, 3]))

    def test_same_order_different_elements(self):
        self.assertFalse(same_order([1, 2, 3], [3, 2, 1]))

    def test_same_order_different_order_same_elements(self):
        self.assertTrue(same_order([1, 2, 3], [3, 1, 2]))

    def test_same_order_different_elements_different_order(self):
        self.assertFalse(same_order([1, 2, 3], [4, 5, 6]))

    def test_same_order_empty_lists(self):
        self.assertTrue(same_order([], []))

    def test_same_order_one_empty_list(self):
        self.assertFalse(same_order([1, 2, 3], []))

    def test_same_order_one_element_lists(self):
        self.assertTrue(same_order([1], [1]))
        self.assertFalse(same_order([1], [2]))

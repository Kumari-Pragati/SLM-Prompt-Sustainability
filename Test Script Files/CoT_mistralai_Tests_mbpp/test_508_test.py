import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):

    def test_same_order_same_lists(self):
        self.assertTrue(same_order([1, 2, 3], [1, 2, 3]))
        self.assertTrue(same_order(["a", "b", "c"], ["c", "b", "a"]))

    def test_same_order_empty_lists(self):
        self.assertTrue(same_order([], []))

    def test_same_order_single_element(self):
        self.assertTrue(same_order([1], [1]))
        self.assertFalse(same_order([1], []))

    def test_same_order_different_order_same_elements(self):
        self.assertFalse(same_order([1, 2, 3], [3, 2, 1]))
        self.assertFalse(same_order(["a", "b", "c"], ["c", "a", "b"]))

    def test_same_order_different_elements(self):
        self.assertFalse(same_order([1, 2, 3], [1, 2, 4]))
        self.assertFalse(same_order(["a", "b", "c"], ["a", "d", "b"]))

    def test_same_order_invalid_inputs(self):
        self.assertRaises(TypeError, same_order, 1, 2)
        self.assertRaises(TypeError, same_order, [1, 2], "list")

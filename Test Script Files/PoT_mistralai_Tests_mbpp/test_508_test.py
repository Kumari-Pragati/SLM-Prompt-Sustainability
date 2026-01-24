import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):
    def test_same_order_typical(self):
        self.assertTrue(same_order([1, 2, 3], [3, 2, 1]))
        self.assertTrue(same_order(["a", "b", "c"], ["c", "b", "a"]))
        self.assertTrue(same_order([1.0, 2.0, 3.0], [3.0, 2.0, 1.0]))

    def test_same_order_edge_cases(self):
        self.assertFalse(same_order([1, 2, 3], [3, 2, 4]))
        self.assertFalse(same_order(["a", "b", "c"], ["c", "b", "d"]))
        self.assertFalse(same_order([1.0, 2.0, 3.0], [3.0, 2.0, 4.0]))
        self.assertFalse(same_order([], []))
        self.assertFalse(same_order([1], []))
        self.assertFalse(same_order([1], [2]))

    def test_same_order_corner_cases(self):
        self.assertTrue(same_order([1, 1, 2], [2, 1, 1]))
        self.assertTrue(same_order([1, 1, 2], [1, 2, 1]))
        self.assertTrue(same_order([1, 1, 2], [2, 1, 2]))
        self.assertFalse(same_order([1, 1, 2], [2, 2, 1]))
        self.assertFalse(same_order([1, 1, 2], [1, 2, 2]))

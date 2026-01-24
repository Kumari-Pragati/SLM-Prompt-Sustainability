import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):

    def test_same_order_normal(self):
        self.assertTrue(same_order([1, 2, 3], [3, 2, 1]))
        self.assertTrue(same_order(["a", "b", "c"], ["c", "b", "a"]))

    def test_same_order_edge_cases(self):
        self.assertFalse(same_order([1, 2, 3], [3, 2, 4]))
        self.assertFalse(same_order(["a", "b", "c"], ["c", "b", "d"]))
        self.assertFalse(same_order([], []))
        self.assertFalse(same_order([1], [2]))
        self.assertFalse(same_order(["a"], ["b"]))

    def test_same_order_empty_intersection(self):
        self.assertFalse(same_order([1, 2, 3], [4, 5, 6]))
        self.assertFalse(same_order(["a", "b", "c"], ["d", "e", "f"]))

    def test_same_order_single_element(self):
        self.assertTrue(same_order([1], [1]))
        self.assertTrue(same_order(["a"], ["a"]))

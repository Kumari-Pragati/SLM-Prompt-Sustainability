import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(same_order([1, 2, 3], [3, 2, 1]))
        self.assertTrue(same_order(["a", "b", "c"], ["c", "b", "a"]))

    def test_edge_cases(self):
        self.assertFalse(same_order([1, 2, 3], [3, 2, 4]))
        self.assertFalse(same_order(["a", "b", "c"], ["c", "b", "d"]))
        self.assertTrue(same_order([], []))
        self.assertTrue(same_order([1], [1]))
        self.assertTrue(same_order(["a"], ["a"]))

    def test_complex(self):
        self.assertTrue(same_order([1, 2, 1], [1, 2, 1]))
        self.assertFalse(same_order([1, 2, 1], [1, 2, 3]))
        self.assertTrue(same_order(["a", "b", "a"], ["a", "b", "a"]))
        self.assertFalse(same_order(["a", "b", "a"], ["a", "b", "c"]))

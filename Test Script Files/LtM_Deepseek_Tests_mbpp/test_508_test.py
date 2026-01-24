import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(same_order([1, 2, 3], [2, 3, 1]))
        self.assertFalse(same_order([1, 2, 3], [3, 2, 1]))

    def test_edge_conditions(self):
        self.assertTrue(same_order([], []))
        self.assertFalse(same_order([1], []))
        self.assertFalse(same_order([], [1]))
        self.assertTrue(same_order([1, 1, 1], [1, 1, 1]))

    def test_complex_cases(self):
        self.assertFalse(same_order([1, 2, 3], [1, 2, 4]))
        self.assertFalse(same_order([1, 2, 2], [2, 1, 1]))
        self.assertFalse(same_order([1, 2, 2], [2, 2, 1]))
        self.assertFalse(same_order([1, 2, 3], [1, 2, 3, 4]))
        self.assertFalse(same_order([1, 2, 3, 4], [1, 2, 3]))

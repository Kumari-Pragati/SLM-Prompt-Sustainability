import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(same_order([1, 2, 3], [3, 2, 1]))
        self.assertFalse(same_order([1, 2, 3], [3, 2, 4]))
        self.assertTrue(same_order([], []))

    def test_edge_cases(self):
        self.assertTrue(same_order([1], [1]))
        self.assertFalse(same_order([1], [2]))
        self.assertTrue(same_order([1, 2, 2, 3], [3, 2, 2, 1]))
        self.assertFalse(same_order([1, 2, 2, 3], [3, 2, 2, 4]))

    def test_corner_cases(self):
        self.assertTrue(same_order([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
        self.assertFalse(same_order([1, 2, 3, 4, 5], [5, 4, 3, 2, 6]))
        self.assertTrue(same_order([], []))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            same_order([1, 2, 3], [3, 2, '1'])
        with self.assertRaises(TypeError):
            same_order([1, 2, '3'], [3, 2, 1])
        with self.assertRaises(TypeError):
            same_order([1, 2, None], [3, 2, 1])

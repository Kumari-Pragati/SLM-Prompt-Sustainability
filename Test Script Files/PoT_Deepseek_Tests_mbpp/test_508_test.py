import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(same_order([1, 2, 3], [2, 3, 1]))
        self.assertTrue(same_order(['a', 'b', 'c'], ['b', 'c', 'a']))
        self.assertFalse(same_order([1, 2, 3], [3, 2, 1]))
        self.assertFalse(same_order(['a', 'b', 'c'], ['b', 'a', 'c']))

    def test_edge_cases(self):
        self.assertTrue(same_order([], []))
        self.assertFalse(same_order([1], [2]))
        self.assertFalse(same_order([1, 2, 3], []))
        self.assertFalse(same_order([], [1, 2, 3]))

    def test_corner_cases(self):
        self.assertTrue(same_order([1, 1, 2, 2], [2, 2, 1, 1]))
        self.assertFalse(same_order([1, 2, 2, 1], [2, 1, 1, 2]))
        self.assertTrue(same_order(['a', 'a', 'b', 'b'], ['b', 'b', 'a', 'a']))
        self.assertFalse(same_order(['a', 'b', 'b', 'a'], ['b', 'a', 'a', 'b']))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            same_order([1, 2, 3], [2, 'a', 1])
        with self.assertRaises(TypeError):
            same_order([1, 'a', 3], [2, 3, 1])

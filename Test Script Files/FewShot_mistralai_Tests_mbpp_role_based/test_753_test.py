import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 6), (7, 8)], 2), [((1, 2),), ((3, 4),)])
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 6), (7, 8)], 4), [((1, 2),), ((3, 4),), ((5, 6),), ((7, 8),)])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(min_k([], 1), [])
        self.assertEqual(min_k([(1, 2)], 1), [((1, 2),)])
        self.assertEqual(min_k([(1, 2)], 2), [((1, 2),)])
        self.assertEqual(min_k([(1, 2), (1, 2)], 1), [((1, 2),)])
        self.assertEqual(min_k([(1, 2), (1, 2)], 2), [((1, 2),), ((1, 2),)])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, min_k, [(1, 2)], 'K')
        self.assertRaises(TypeError, min_k, [(1, 2)], -1)

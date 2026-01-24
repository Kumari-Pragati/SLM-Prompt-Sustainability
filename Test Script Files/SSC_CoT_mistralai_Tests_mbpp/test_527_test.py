import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4], 4, 5), 1)
        self.assertEqual(get_pairs_count([10, 15, 3, 7], 4, 13), 1)

    def test_edge_cases(self):
        self.assertEqual(get_pairs_count([], 0, 10), 0)
        self.assertEqual(get_pairs_count([1], 1, 2), 0)
        self.assertEqual(get_pairs_count([1, 2], 2, 3), 0)
        self.assertEqual(get_pairs_count([1, 2], 2, 4), 1)
        self.assertEqual(get_pairs_count([1, 2], 2, 5), 0)

    def test_boundary_cases(self):
        self.assertEqual(get_pairs_count([1, 2], 2, 1), 0)
        self.assertEqual(get_pairs_count([1, 2], 2, 0), 0)
        self.assertEqual(get_pairs_count([1, 2], 2, -1), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, get_pairs_count, [], 0, 10, 'invalid_type')
        self.assertRaises(TypeError, get_pairs_count, [1], 0, 10, 1.5)
        self.assertRaises(TypeError, get_pairs_count, [1], -1, 10, 10)

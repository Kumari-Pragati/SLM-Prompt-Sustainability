import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 6)], 2), [((1, 2),), ((3, 4),)])
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 6)], 1), [((1, 2),)])

    def test_edge_cases(self):
        self.assertEqual(min_k([], 1), [])
        self.assertEqual(min_k([(1, 2)], 1), [((1, 2),)])
        self.assertEqual(min_k([(1, 2), (1, 2)], 2), [((1, 2),), ((1, 2),)])

    def test_boundary_cases(self):
        self.assertEqual(min_k([(1, 2), (1, 1), (1, 3)], 2), [((1, 1),), ((1, 2),)])
        self.assertEqual(min_k([(1, 2), (1, 1), (1, 3)], 3), [((1, 1),), ((1, 2),), ((1, 3),)])

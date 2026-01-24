import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 1)], 2), [(5, 1), (3, 4)])
        self.assertEqual(min_k([(1, 2), (3, 1), (5, 3)], 1), [(1, 2)])

    def test_edge_conditions(self):
        self.assertEqual(min_k([], 2), [])
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 1)], 0), [])
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 1)], 4), [(1, 2), (3, 4), (5, 1)])

    def test_complex_cases(self):
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 1), (7, 2)], 3), [(5, 1), (7, 2), (3, 4)])
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 1), (7, 2)], 2), [(7, 2), (5, 1)])

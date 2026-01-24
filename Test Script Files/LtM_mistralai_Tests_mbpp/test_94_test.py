import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(index_minimum([(1, 2), (3, 4), (2, 1)]), (1, 2))
        self.assertEqual(index_minimum([(0, 0), (1, 1), (2, 2)]), (0, 0))
        self.assertEqual(index_minimum([(100, 1), (200, 2), (300, 3)]), (1, 1))

    def test_edge_cases(self):
        self.assertEqual(index_minimum([(1, 2), (1, 1), (1, 3)]), (1, 1))
        self.assertEqual(index_minimum([(1, 2), (1, 1), (2, 1)]), (1, 1))
        self.assertEqual(index_minimum([(1, 2), (1, 1), (1, float('inf'))]), (1, 1))
        self.assertEqual(index_minimum([(1, 2), (1, 1), (1, -1)]), (1, 1))
        self.assertEqual(index_minimum([]), None)

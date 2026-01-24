import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(index_minimum([(1, 2), (3, 4), (1, 3)]), (1, 2))
        self.assertEqual(index_minimum([(0, 0), (1, 1), (2, 2)]), (0, 0))
        self.assertEqual(index_minimum([(100, 1), (3, 4), (1, 300)]), (1, 300))

    def test_edge_case(self):
        self.assertEqual(index_minimum([(1, 2), (1, 1), (1, 3)]), (1, 1))
        self.assertEqual(index_minimum([(1, 2), (1, 2), (1, 3)]), (1, 2))
        self.assertEqual(index_minimum([(1, 2), (1, 2), (2, 2)]), (1, 2))

    def test_boundary_case(self):
        self.assertEqual(index_minimum([(1, 2), (1, 2), (1, 2), (1, 2)]), (1, 2))
        self.assertEqual(index_minimum([(1, 2), (1, 2), (1, 2), (2, 2)]), (1, 2))
        self.assertEqual(index_minimum([(1, 2), (1, 2), (1, 2), (1, -1)]), (1, 2))

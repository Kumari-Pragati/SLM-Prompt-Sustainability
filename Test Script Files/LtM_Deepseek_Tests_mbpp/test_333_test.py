import unittest
from mbpp_333_code import Sort

class TestSortFunction(unittest.TestCase):

    def test_simple_sort(self):
        self.assertEqual(Sort([(1, 2), (3, 4), (5, 1)]), [(5, 1), (1, 2), (3, 4)])

    def test_edge_sort(self):
        self.assertEqual(Sort([]), [])
        self.assertEqual(Sort([(1, 2)]), [(1, 2)])

    def test_boundary_sort(self):
        self.assertEqual(Sort([(1, 1), (2, 2), (3, 3)]), [(3, 3), (2, 2), (1, 1)])
        self.assertEqual(Sort([(1, 1000), (2, 1), (3, 2)]), [(3, 2), (1, 1000), (2, 1)])

    def test_complex_sort(self):
        self.assertEqual(Sort([(1, 2), (2, 1), (3, 3), (4, 2)]), [(4, 2), (1, 2), (3, 3), (2, 1)])
        self.assertEqual(Sort([(1, 1), (2, 2), (3, 3), (4, 4)]), [(4, 4), (3, 3), (2, 2), (1, 1)])

import unittest
from mbpp_71_code import comb_sort

class TestCombSort(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(comb_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(comb_sort([1]), [1])
        self.assertEqual(comb_sort([1, 1]), [1, 1])

    def test_edge_and_boundary(self):
        self.assertEqual(comb_sort([]), [])
        self.assertEqual(comb_sort([float('inf'), float('inf')]), [float('inf'), float('inf')])
        self.assertEqual(comb_sort([-float('inf'), -float('inf')]), [-float('inf'), -float('inf')])

    def test_complex_input(self):
        self.assertEqual(comb_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(comb_sort([5, 4, 3, 2, 1, 0]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(comb_sort([5, 4, 3, 2, 1, 0, -1]), [-1, 0, 1, 2, 3, 4, 5])

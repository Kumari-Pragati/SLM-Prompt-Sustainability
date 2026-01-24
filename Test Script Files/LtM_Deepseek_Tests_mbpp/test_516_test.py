import unittest
from mbpp_516_code import radix_sort

class TestRadixSort(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(radix_sort([10, 2, 3, 4, 5]), [2, 3, 4, 5, 10])
        self.assertEqual(radix_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(radix_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(radix_sort([0]), [0])
        self.assertEqual(radix_sort([]), [])
        self.assertEqual(radix_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_more_complex_or_corner_cases(self):
        self.assertEqual(radix_sort([10, 20, 30, 40, 50]), [10, 20, 30, 40, 50])
        self.assertEqual(radix_sort([100, 200, 300, 400, 500]), [100, 200, 300, 400, 500])
        self.assertEqual(radix_sort([1000, 2000, 3000, 4000, 5000]), [1000, 2000, 3000, 4000, 5000])

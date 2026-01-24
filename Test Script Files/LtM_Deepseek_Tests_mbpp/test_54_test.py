import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(counting_sort([1, 4, 1, 2, 7, 5, 2]), [1, 1, 2, 2, 4, 5, 7])
        self.assertEqual(counting_sort([5, 3, 2, 1, 4]), [1, 2, 3, 4, 5])

    def test_edge_conditions(self):
        self.assertEqual(counting_sort([]), [])
        self.assertEqual(counting_sort([0]), [0])
        self.assertEqual(counting_sort([1]), [1])

    def test_boundary_conditions(self):
        self.assertEqual(counting_sort([0, 0, 0, 0]), [0, 0, 0, 0])
        self.assertEqual(counting_sort([99, 99, 99, 99]), [99, 99, 99, 99])

    def test_complex_cases(self):
        self.assertEqual(counting_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(counting_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

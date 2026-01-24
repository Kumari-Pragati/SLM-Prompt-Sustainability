import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(counting_sort([4, 2, 2, 8, 3, 3, 1]), [1, 2, 2, 3, 3, 4, 8])

    def test_edge_case_single_element(self):
        self.assertEqual(counting_sort([5]), [5])

    def test_edge_case_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_boundary_case_max_value(self):
        self.assertEqual(counting_sort([0, 1, 2, 3, 4, 5]), [0, 1, 2, 3, 4, 5])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(counting_sort([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])

    def test_corner_case_mixed_positive_negative(self):
        self.assertEqual(counting_sort([-1, 2, -3, 4, -5]), [-5, -3, -1, 2, 4])

    def test_corner_case_duplicates(self):
        self.assertEqual(counting_sort([2, 2, 2, 1, 1, 1]), [1, 1, 1, 2, 2, 2])

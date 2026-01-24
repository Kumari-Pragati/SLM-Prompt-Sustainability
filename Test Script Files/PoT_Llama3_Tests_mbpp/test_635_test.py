import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(heap_sort([1]), [1])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(heap_sort([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])

    def test_edge_case_duplicates(self):
        self.assertEqual(heap_sort([1, 2, 2, 3, 3, 3, 4, 5]), [1, 2, 2, 3, 3, 3, 4, 5])

    def test_edge_case_large_numbers(self):
        self.assertEqual(heap_sort([100, 200, 300, 400, 500]), [100, 200, 300, 400, 500])

    def test_edge_case_negative_and_positive_numbers(self):
        self.assertEqual(heap_sort([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]), [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

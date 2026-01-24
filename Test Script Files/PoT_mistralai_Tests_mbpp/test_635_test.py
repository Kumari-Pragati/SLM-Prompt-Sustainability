import unittest
from mbpp_635_code import heap_sort

class TestHeapSort(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(heap_sort([3, 5, 1, 7, 2]), [1, 2, 3, 5, 7])
        self.assertEqual(heap_sort([10, 20, 30, 40, 50]), [10, 20, 30, 40, 50])
        self.assertEqual(heap_sort([1, -1, 0]), [-1, 0, 1])

    def test_edge_case_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(heap_sort([4]), [4])

    def test_edge_case_duplicates(self):
        self.assertEqual(heap_sort([1, 1, 2, 3]), [1, 1, 2, 3])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(heap_sort([-1, -2, -3]), [-3, -2, -1])

    def test_corner_case_mixed_signs(self):
        self.assertEqual(heap_sort([-1, 1, -2, 2]), [-2, -1, 1, 2])

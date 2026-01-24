import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(heap_replace([3, 5, 1, 7, 9], 6), [3, 5, 6, 7, 9])
        self.assertListEqual(heap_replace([], 1), [1])
        self.assertListEqual(heap_replace([1], 2), [2])
        self.assertListEqual(heap_replace([1, 2], 3), [1, 2, 3])

    def test_edge_case_empty_heap(self):
        self.assertListEqual(heap_replace([], 1), [1])

    def test_edge_case_single_element(self):
        self.assertListEqual(heap_replace([1], 2), [2])

    def test_edge_case_single_element_heapify(self):
        self.assertListEqual(heap_replace([2], 1), [1])

    def test_edge_case_duplicate_element(self):
        self.assertListEqual(heap_replace([1, 1], 2), [1, 2])

    def test_edge_case_max_heap(self):
        self.assertListEqual(heap_replace([10, 9, 8, 7, 6], 5), [10, 9, 8, 7, 5])

    def test_edge_case_min_heap(self):
        self.assertListEqual(heap_replace([1, 2, 3], 0), [0, 1, 2])

    def test_corner_case_negative_numbers(self):
        self.assertListEqual(heap_replace([-1, -2, -3], -4), [-1, -2, -3])
        self.assertListEqual(heap_replace([-1, -2, -3], -5), [-5, -1, -2])

import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):

    def test_empty_heap(self):
        self.assertListEqual(heap_replace([]), [])

    def test_single_element_heap(self):
        self.assertListEqual(heap_replace([1]), [1])

    def test_multiple_elements_heap(self):
        self.assertListEqual(heap_replace([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_heapify_and_heapreplace(self):
        self.assertListEqual(heap_replace([7, 5, 3, 1]), [1, 3, 5, 7])

    def test_negative_numbers(self):
        self.assertListEqual(heap_replace([-1, -3, -5, -7]), [-7, -5, -3, -1])

    def test_duplicate_values(self):
        self.assertListEqual(heap_replace([1, 1, 3, 5, 7]), [1, 3, 5, 7])

    def test_large_numbers(self):
        self.assertListEqual(heap_replace([1000000001, 999999999, 1000000002, 999999998]), [999999998, 999999999, 1000000001, 1000000002])

    def test_heapify_with_empty_list(self):
        self.assertRaises(ValueError, heap_replace, [], 1)

    def test_heapreplace_with_empty_list(self):
        self.assertRaises(ValueError, heap_replace, [1], [])

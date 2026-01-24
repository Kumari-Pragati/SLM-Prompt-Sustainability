import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):

    def test_typical_case(self):
        heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        a = 7
        expected_heap = [3, 1, 4, 1, 5, 7, 2, 6, 5, 3, 5]
        self.assertEqual(heap_replace(heap, a), expected_heap)

    def test_empty_heap(self):
        heap = []
        a = 10
        expected_heap = [10]
        self.assertEqual(heap_replace(heap, a), expected_heap)

    def test_single_element_heap(self):
        heap = [5]
        a = 10
        expected_heap = [10]
        self.assertEqual(heap_replace(heap, a), expected_heap)

    def test_replace_smallest_element(self):
        heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        a = 0
        expected_heap = [0, 1, 1, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(heap_replace(heap, a), expected_heap)

    def test_replace_largest_element(self):
        heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        a = 10
        expected_heap = [3, 1, 4, 1, 5, 10, 2, 6, 5, 3, 5]
        self.assertEqual(heap_replace(heap, a), expected_heap)

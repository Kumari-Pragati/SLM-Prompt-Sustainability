import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):

    def test_simple_input(self):
        heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        a = 7
        expected_heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 7]
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

    def test_maximum_value(self):
        heap = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        a = 11
        expected_heap = [11, 10, 8, 7, 6, 5, 4, 3, 2, 1, 9]
        self.assertEqual(heap_replace(heap, a), expected_heap)

    def test_minimum_value(self):
        heap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        a = 0
        expected_heap = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 2]
        self.assertEqual(heap_replace(heap, a), expected_heap)

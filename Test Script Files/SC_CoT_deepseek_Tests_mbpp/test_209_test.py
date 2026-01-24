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

    def test_largest_element(self):
        heap = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        a = 15
        expected_heap = [10, 9, 8, 7, 6, 5, 4, 3, 2, 15]
        self.assertEqual(heap_replace(heap, a), expected_heap)

    def test_smallest_element(self):
        heap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        a = -1
        expected_heap = [-1, 1, 3, 2, 5, 6, 7, 8, 9, 10]
        self.assertEqual(heap_replace(heap, a), expected_heap)

    def test_invalid_input(self):
        heap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        a = 'a'
        with self.assertRaises(TypeError):
            heap_replace(heap, a)

import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):

    def test_normal_usage(self):
        heap = [3, 5, 1, 7, 9]
        result = heap_replace(heap, 2)
        self.assertEqual(result, [2, 3, 5, 1, 7, 9])

    def test_empty_heap(self):
        result = heap_replace([], 1)
        self.assertEqual(result, [1])

    def test_single_element_heap(self):
        result = heap_replace([4], 2)
        self.assertEqual(result, [2, 4])

    def test_negative_numbers(self):
        heap = [-3, -5, -1, -7, -9]
        result = heap_replace(heap, -2)
        self.assertEqual(result, [-2, -3, -5, -1, -7, -9])

    def test_float_numbers(self):
        heap = [3.14, 5.5, 1.01, 7.07, 9.99]
        result = heap_replace(heap, 2.22)
        self.assertEqual(result, [2.22, 3.14, 5.5, 1.01, 7.07, 9.99])

    def test_large_numbers(self):
        heap = [1000000000000000000, 5, 1, 7, 9]
        result = heap_replace(heap, 2)
        self.assertEqual(result, [2, 1000000000000000000, 5, 1, 7, 9])

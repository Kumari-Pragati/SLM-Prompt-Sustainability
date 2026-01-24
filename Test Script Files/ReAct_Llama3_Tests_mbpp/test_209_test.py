import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):

    def test_typical_case(self):
        heap = [1, 3, 5, 7, 9]
        result = heap_replace(heap, 2)
        self.assertEqual(result, [1, 2, 3, 5, 7, 9])

    def test_edge_case_empty_heap(self):
        heap = []
        result = heap_replace(heap, 1)
        self.assertEqual(result, [1])

    def test_edge_case_single_element_heap(self):
        heap = [1]
        result = heap_replace(heap, 2)
        self.assertEqual(result, [2])

    def test_edge_case_max_heap(self):
        heap = [10, 20, 30, 40, 50]
        result = heap_replace(heap, 60)
        self.assertEqual(result, [10, 20, 30, 40, 50, 60])

    def test_edge_case_min_heap(self):
        heap = [10, 20, 30, 40, 50]
        result = heap_replace(heap, 5)
        self.assertEqual(result, [5, 10, 20, 30, 40, 50])

    def test_error_case_non_list_input(self):
        with self.assertRaises(TypeError):
            heap_replace(None, 1)

    def test_error_case_non_integer_input(self):
        with self.assertRaises(TypeError):
            heap_replace([1, 2, 3], 'a')

import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):
    def test_typical_use_case(self):
        heap = [1, 3, 5, 7, 9]
        heap_replace(heap, 2)
        self.assertEqual(heap, [1, 2, 5, 7, 9])

    def test_edge_case_empty_heap(self):
        heap = []
        heap_replace(heap, 1)
        self.assertEqual(heap, [1])

    def test_edge_case_single_element_heap(self):
        heap = [1]
        heap_replace(heap, 2)
        self.assertEqual(heap, [2])

    def test_edge_case_heap_with_duplicates(self):
        heap = [1, 2, 2, 3, 4]
        heap_replace(heap, 2)
        self.assertEqual(heap, [1, 2, 2, 3, 4])

    def test_edge_case_heap_with_negative_numbers(self):
        heap = [-1, -2, -3, -4, -5]
        heap_replace(heap, -3)
        self.assertEqual(heap, [-5, -4, -3, -2, -1])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            heap_replace(None, 1)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            heap_replace([1, 2, 3], 'a')

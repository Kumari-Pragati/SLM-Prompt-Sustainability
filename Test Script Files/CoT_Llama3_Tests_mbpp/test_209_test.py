import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):
    def test_typical_input(self):
        heap = [1, 3, 5, 7, 9]
        a = 2
        result = heap_replace(heap, a)
        self.assertEqual(result, [1, 2, 5, 7, 9])

    def test_edge_case_empty_heap(self):
        heap = []
        a = 1
        result = heap_replace(heap, a)
        self.assertEqual(result, [1])

    def test_edge_case_single_element_heap(self):
        heap = [1]
        a = 2
        result = heap_replace(heap, a)
        self.assertEqual(result, [2])

    def test_edge_case_heap_with_duplicates(self):
        heap = [1, 2, 2, 3, 4]
        a = 2
        result = heap_replace(heap, a)
        self.assertEqual(result, [1, 2, 2, 3, 4])

    def test_invalid_input_non_integer(self):
        heap = [1, 2, 3]
        a = 'a'
        with self.assertRaises(TypeError):
            heap_replace(heap, a)

    def test_invalid_input_non_list(self):
        heap = 'not a list'
        a = 1
        with self.assertRaises(TypeError):
            heap_replace(heap, a)

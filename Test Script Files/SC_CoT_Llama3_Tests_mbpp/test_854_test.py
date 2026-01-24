import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):

    def test_typical_input(self):
        rawheap = [5, 3, 8, 2, 1]
        result = raw_heap(rawheap)
        self.assertEqual(result, [1, 2, 3, 5, 8])

    def test_edge_case_empty_list(self):
        rawheap = []
        result = raw_heap(rawheap)
        self.assertEqual(result, [])

    def test_edge_case_single_element_list(self):
        rawheap = [5]
        result = raw_heap(rawheap)
        self.assertEqual(result, [5])

    def test_edge_case_list_with_duplicates(self):
        rawheap = [5, 5, 3, 8, 2, 1]
        result = raw_heap(rawheap)
        self.assertEqual(result, [1, 2, 3, 5, 5, 8])

    def test_edge_case_negative_numbers(self):
        rawheap = [-5, 3, -8, 2, 1]
        result = raw_heap(rawheap)
        self.assertEqual(result, [-8, -5, 1, 2, 3])

    def test_edge_case_mixed_numbers(self):
        rawheap = [5, -3, 8, 2, 1]
        result = raw_heap(rawheap)
        self.assertEqual(result, [-3, 1, 2, 5, 8])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            raw_heap("invalid input")

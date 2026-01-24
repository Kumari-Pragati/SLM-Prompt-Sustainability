import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):

    def test_typical_case(self):
        heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        a = 7
        expected_heap = [7, 1, 5, 1, 3, 9, 2, 6, 5, 3, 4]
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

    def test_same_value_replacement(self):
        heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        a = 3
        expected_heap = [3, 1, 4, 1, 3, 9, 2, 6, 5, 3, 5]
        self.assertEqual(heap_replace(heap, a), expected_heap)

    def test_invalid_input(self):
        heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        a = 'a'
        with self.assertRaises(TypeError):
            heap_replace(heap, a)

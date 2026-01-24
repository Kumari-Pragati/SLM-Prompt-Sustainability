import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):
    def test_typical_use_case(self):
        heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        a = 10
        expected_heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 10]
        self.assertEqual(heap_replace(heap, a), expected_heap)

    def test_edge_condition(self):
        heap = []
        a = 10
        expected_heap = [10]
        self.assertEqual(heap_replace(heap, a), expected_heap)

    def test_boundary_condition(self):
        heap = [10]
        a = 1
        expected_heap = [1]
        self.assertEqual(heap_replace(heap, a), expected_heap)

    def test_invalid_input(self):
        heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        a = 'a'
        with self.assertRaises(TypeError):
            heap_replace(heap, a)

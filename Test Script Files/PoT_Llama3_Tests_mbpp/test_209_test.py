import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):

    def test_typical_case(self):
        heap = [1, 3, 5, 7, 9]
        a = 2
        expected = [1, 2, 5, 7, 9]
        self.assertEqual(heap_replace(heap, a), expected)

    def test_edge_case_min(self):
        heap = [1, 3, 5, 7, 9]
        a = 0
        expected = [0, 1, 3, 5, 7]
        self.assertEqual(heap_replace(heap, a), expected)

    def test_edge_case_max(self):
        heap = [1, 3, 5, 7, 9]
        a = 10
        expected = [1, 3, 5, 7, 10]
        self.assertEqual(heap_replace(heap, a), expected)

    def test_edge_case_replace_min(self):
        heap = [1, 3, 5, 7, 9]
        a = 1
        expected = [1, 1, 5, 7, 9]
        self.assertEqual(heap_replace(heap, a), expected)

    def test_edge_case_replace_max(self):
        heap = [1, 3, 5, 7, 9]
        a = 9
        expected = [1, 3, 5, 7, 9]
        self.assertEqual(heap_replace(heap, a), expected)

    def test_invalid_input(self):
        heap = [1, 3, 5, 7, 9]
        a = 'a'
        with self.assertRaises(TypeError):
            heap_replace(heap, a)

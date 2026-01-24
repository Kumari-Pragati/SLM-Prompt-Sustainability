import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):
    def test_heap_replace_positive(self):
        heap = [5, 3, 1, 4, 2]
        result = heap_replace(heap, 0)
        self.assertEqual(result, [0, 3, 1, 4, 2])

    def test_heap_replace_empty(self):
        heap = []
        result = heap_replace(heap, 0)
        self.assertEqual(result, [0])

    def test_heap_replace_single_element(self):
        heap = [1]
        result = heap_replace(heap, 0)
        self.assertEqual(result, [0])

    def test_heap_replace_negative(self):
        heap = [-5, -3, -1, -4, -2]
        result = heap_replace(heap, 0)
        self.assertEqual(result, [0, -3, -1, -4, -2])

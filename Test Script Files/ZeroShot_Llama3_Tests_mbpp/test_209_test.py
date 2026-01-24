import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):

    def test_heap_replace(self):
        heap = [1, 3, 5, 7, 9]
        heap_replace(heap, 2)
        self.assertEqual(heap, [2, 1, 3, 5, 7])
        heap = [1, 3, 5, 7, 9]
        heap_replace(heap, 10)
        self.assertEqual(heap, [10, 1, 3, 5, 7])
        heap = [1, 3, 5, 7, 9]
        heap_replace(heap, 8)
        self.assertEqual(heap, [8, 1, 3, 5, 7])
        heap = [1, 3, 5, 7, 9]
        heap_replace(heap, 6)
        self.assertEqual(heap, [6, 1, 3, 5, 7])
        heap = [1, 3, 5, 7, 9]
        heap_replace(heap, 4)
        self.assertEqual(heap, [4, 1, 3, 5, 7])
        heap = [1, 3, 5, 7, 9]
        heap_replace(heap, 0)
        self.assertEqual(heap, [0, 1, 3, 5, 7])

    def test_heap_replace_empty_heap(self):
        heap = []
        heap_replace(heap, 2)
        self.assertEqual(heap, [2])

    def test_heap_replace_single_element_heap(self):
        heap = [1]
        heap_replace(heap, 2)
        self.assertEqual(heap, [2])

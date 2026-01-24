import unittest
from mbpp_209_code import heapify, heapreplace

class TestHeapReplace(unittest.TestCase):

    def test_heap_replace_empty(self):
        self.assertListEqual(heap_replace([], 1), [1])

    def test_heap_replace_single_element(self):
        self.assertListEqual(heap_replace([2], 1), [1, 2])

    def test_heap_replace_multiple_elements(self):
        self.assertListEqual(heap_replace([3, 1, 5, 2], 7), [3, 5, 7, 1, 2])

    def test_heap_replace_with_duplicates(self):
        self.assertListEqual(heap_replace([3, 1, 5, 2, 3], 7), [3, 5, 7, 1, 3, 2])

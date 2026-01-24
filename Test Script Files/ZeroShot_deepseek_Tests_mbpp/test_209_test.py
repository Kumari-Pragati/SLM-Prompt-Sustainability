import unittest
from mbpp_209_code import heapify, heapreplace
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):

    def test_heap_replace(self):
        # Test with a list that is already a heap
        heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        heap_replace(heap, 10)
        self.assertEqual(heap[0], 10)  # The maximum element should be replaced

        # Test with a list that is not a heap
        heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        heapify(heap)
        heap_replace(heap, 10)
        self.assertEqual(heap[0], 10)  # The maximum element should be replaced

        # Test with a list of one element
        heap = [5]
        heap_replace(heap, 10)
        self.assertEqual(heap[0], 10)  # The only element should be replaced

        # Test with a list of two elements, where the second element is greater
        heap = [5, 10]
        heap_replace(heap, 3)
        self.assertEqual(heap[0], 10)  # The maximum element should be replaced

        # Test with a list of two elements, where the first element is greater
        heap = [10, 5]
        heap_replace(heap, 3)
        self.assertEqual(heap[0], 10)  # The maximum element should be replaced

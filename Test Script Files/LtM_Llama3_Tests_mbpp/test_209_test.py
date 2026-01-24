import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):
    def test_simple(self):
        heap = [1, 3, 5, 7, 9]
        a = 2
        result = heap_replace(heap, a)
        self.assertEqual(result, [1, 2, 5, 7, 9])

    def test_empty_heap(self):
        heap = []
        a = 1
        result = heap_replace(heap, a)
        self.assertEqual(result, [1])

    def test_min_value(self):
        heap = [1, 3, 5, 7, 9]
        a = 0
        result = heap_replace(heap, a)
        self.assertEqual(result, [0, 1, 3, 5, 7])

    def test_max_value(self):
        heap = [1, 3, 5, 7, 9]
        a = 10
        result = heap_replace(heap, a)
        self.assertEqual(result, [1, 3, 5, 7, 10])

    def test_heapify(self):
        heap = [1, 3, 5, 7, 9]
        a = 2
        result = heap_replace(heap, a)
        self.assertTrue(hq.isheap(heap))

    def test_heapreplace(self):
        heap = [1, 3, 5, 7, 9]
        a = 2
        result = heap_replace(heap, a)
        self.assertEqual(hq.heappop(heap), 2)

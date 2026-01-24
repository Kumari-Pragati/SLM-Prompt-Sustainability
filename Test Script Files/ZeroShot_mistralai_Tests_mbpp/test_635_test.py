import unittest
from mbpp_635_code import range
import heapq as hq

def heap_sort(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, value)
    return [hq.heappop(h) for i in range(len(h))]

class TestHeapSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element(self):
        self.assertEqual(heap_sort([4]), [4])

    def test_simple_list(self):
        self.assertEqual(heap_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_reverse_list(self):
        self.assertEqual(heap_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_large_list(self):
        data = [x for x in range(100)]
        sorted_data = sorted(data)
        self.assertEqual(heap_sort(data), sorted_data)

    def test_negative_numbers(self):
        data = [-5, -3, -1, 0, 2, 4, 6]
        sorted_data = sorted(data)
        self.assertEqual(heap_sort(data), sorted_data)

    def test_mixed_numbers(self):
        data = [1, 2, -3, 4, -5, 6, -7]
        sorted_data = sorted(data)
        self.assertEqual(heap_sort(data), sorted_data)

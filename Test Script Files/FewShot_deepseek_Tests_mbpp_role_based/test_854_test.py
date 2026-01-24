import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):
    def test_typical_use_case(self):
        rawheap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected_heap = [1, 1, 2, 3, 3, 9, 4, 6, 5, 5, 5]
        self.assertEqual(raw_heap(rawheap), expected_heap)

    def test_empty_list(self):
        rawheap = []
        expected_heap = []
        self.assertEqual(raw_heap(rawheap), expected_heap)

    def test_single_element(self):
        rawheap = [5]
        expected_heap = [5]
        self.assertEqual(raw_heap(rawheap), expected_heap)

    def test_negative_numbers(self):
        rawheap = [-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]
        expected_heap = [-9, -1, -2, -3, -3, -5, -4, -6, -5, -5, -1]
        self.assertEqual(raw_heap(rawheap), expected_heap)

    def test_duplicate_elements(self):
        rawheap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected_heap = [1, 1, 2, 3, 3, 9, 4, 6, 5, 5, 5]
        self.assertEqual(raw_heap(rawheap), expected_heap)

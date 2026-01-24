import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):
    def test_typical_use_case(self):
        rawheap = [5, 2, 8, 1, 9]
        result = raw_heap(rawheap)
        self.assertEqual(result, [1, 2, 5, 8, 9])

    def test_empty_list(self):
        rawheap = []
        result = raw_heap(rawheap)
        self.assertEqual(result, [])

    def test_single_element_list(self):
        rawheap = [5]
        result = raw_heap(rawheap)
        self.assertEqual(result, [5])

    def test_negative_numbers(self):
        rawheap = [-5, -2, -8, -1, -9]
        result = raw_heap(rawheap)
        self.assertEqual(result, [-9, -8, -5, -2, -1])

    def test_mixed_numbers(self):
        rawheap = [5, -2, 8, 1, -9]
        result = raw_heap(rawheap)
        self.assertEqual(result, [-9, 1, 5, 8, -2])

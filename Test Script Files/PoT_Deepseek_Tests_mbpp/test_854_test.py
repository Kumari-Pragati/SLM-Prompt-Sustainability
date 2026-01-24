import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):

    def test_typical_case(self):
        rawheap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected_output = [1, 1, 2, 3, 3, 5, 5, 5, 6, 9, 4]
        self.assertEqual(raw_heap(rawheap), expected_output)

    def test_empty_list(self):
        rawheap = []
        expected_output = []
        self.assertEqual(raw_heap(rawheap), expected_output)

    def test_single_element(self):
        rawheap = [7]
        expected_output = [7]
        self.assertEqual(raw_heap(rawheap), expected_output)

    def test_duplicate_elements(self):
        rawheap = [1, 1, 1, 1]
        expected_output = [1, 1, 1, 1]
        self.assertEqual(raw_heap(rawheap), expected_output)

    def test_negative_numbers(self):
        rawheap = [-1, -3, -2, -4]
        expected_output = [-4, -3, -2, -1]
        self.assertEqual(raw_heap(rawheap), expected_output)

    def test_mixed_numbers(self):
        rawheap = [3, -1, 4, 1, -5, 9, 2, -6, 5, 3, -5]
        expected_output = [-6, -5, -5, -1, 3, 3, 2, 5, 9, 4, 1]
        self.assertEqual(raw_heap(rawheap), expected_output)

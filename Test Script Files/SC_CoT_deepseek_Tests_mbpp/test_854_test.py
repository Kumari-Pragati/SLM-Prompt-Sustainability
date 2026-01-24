import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):

    def test_typical_case(self):
        rawheap = [3, 1, 2]
        expected_output = [1, 3, 2]
        self.assertEqual(raw_heap(rawheap), expected_output)

    def test_empty_list(self):
        rawheap = []
        expected_output = []
        self.assertEqual(raw_heap(rawheap), expected_output)

    def test_single_element(self):
        rawheap = [1]
        expected_output = [1]
        self.assertEqual(raw_heap(rawheap), expected_output)

    def test_duplicate_elements(self):
        rawheap = [3, 1, 2, 1, 2, 3]
        expected_output = [1, 1, 2, 3, 2, 3]
        self.assertEqual(raw_heap(rawheap), expected_output)

    def test_negative_numbers(self):
        rawheap = [-3, -1, -2]
        expected_output = [-3, -1, -2]
        self.assertEqual(raw_heap(rawheap), expected_output)

    def test_mixed_numbers(self):
        rawheap = [3, -1, 2, 0]
        expected_output = [-1, 0, 2, 3]
        self.assertEqual(raw_heap(rawheap), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            raw_heap(123)

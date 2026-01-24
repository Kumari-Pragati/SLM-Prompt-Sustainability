import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(raw_heap([]), [])

    def test_single_element_list(self):
        self.assertEqual(raw_heap([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(raw_heap([3, 2, 1]), [1, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(raw_heap([-3, -2, -1]), [-1, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(raw_heap([1, -2, 3, -4, 5]), [-4, -2, 1, 3, 5])

    def test_list_with_duplicates(self):
        self.assertEqual(raw_heap([1, 1, 2, 2, 3]), [1, 1, 2, 2, 3])

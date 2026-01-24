import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(raw_heap([]), [])

    def test_single_element_input(self):
        self.assertEqual(raw_heap([5]), [5])

    def test_multiple_elements_input(self):
        self.assertEqual(raw_heap([5, 3, 8, 2, 1]), [1, 2, 3, 5, 8])

    def test_negative_elements_input(self):
        self.assertEqual(raw_heap([-5, -3, -8, -2, -1]), [-8, -5, -3, -2, -1])

    def test_max_heap_input(self):
        self.assertEqual(raw_heap([5, 3, 8, 2, 1]), [1, 2, 3, 5, 8])

    def test_min_heap_input(self):
        self.assertEqual(raw_heap([5, 3, 8, 2, 1]), [1, 2, 3, 5, 8])

    def test_heapify_empty_list(self):
        self.assertEqual(raw_heap([]), [])

    def test_heapify_single_element_list(self):
        self.assertEqual(raw_heap([5]), [5])

    def test_heapify_multiple_elements_list(self):
        self.assertEqual(raw_heap([5, 3, 8, 2, 1]), [1, 2, 3, 5, 8])

    def test_heapify_negative_elements_list(self):
        self.assertEqual(raw_heap([-5, -3, -8, -2, -1]), [-8, -5, -3, -2, -1])

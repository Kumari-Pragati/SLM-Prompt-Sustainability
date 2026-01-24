import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):

    def test_heapify(self):
        self.assertEqual(raw_heap([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_heapify_empty(self):
        self.assertEqual(raw_heap([]), [])

    def test_heapify_single_element(self):
        self.assertEqual(raw_heap([1]), [1])

    def test_heapify_multiple_elements(self):
        self.assertEqual(raw_heap([5, 3, 8, 4, 2, 6, 1]), [8, 6, 5, 4, 3, 2, 1])

    def test_heapify_duplicates(self):
        self.assertEqual(raw_heap([5, 3, 8, 4, 4, 2, 1]), [8, 4, 4, 3, 2, 1, 5])

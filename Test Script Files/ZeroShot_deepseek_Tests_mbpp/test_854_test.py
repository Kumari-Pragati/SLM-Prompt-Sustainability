import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(raw_heap([]), [])

    def test_single_element(self):
        self.assertEqual(raw_heap([1]), [1])

    def test_multiple_elements(self):
        self.assertEqual(raw_heap([3, 1, 2]), [1, 3, 2])
        self.assertEqual(raw_heap([3, 2, 1]), [1, 2, 3])
        self.assertEqual(raw_heap([1, 2, 3]), [1, 2, 3])

    def test_duplicate_elements(self):
        self.assertEqual(raw_heap([3, 1, 2, 1]), [1, 2, 3, 1])
        self.assertEqual(raw_heap([3, 2, 1, 2]), [1, 2, 3, 2])
        self.assertEqual(raw_heap([1, 2, 3, 1]), [1, 2, 3, 1])

    def test_negative_elements(self):
        self.assertEqual(raw_heap([-3, -1, -2]), [-3, -1, -2])
        self.assertEqual(raw_heap([-3, -2, -1]), [-3, -2, -1])
        self.assertEqual(raw_heap([-1, -2, -3]), [-3, -2, -1])

    def test_mixed_elements(self):
        self.assertEqual(raw_heap([3, -1, 2]), [-1, 2, 3])
        self.assertEqual(raw_heap([3, -2, 1]), [-2, 1, 3])
        self.assertEqual(raw_heap([1, -2, 3]), [-2, 1, 3])

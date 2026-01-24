import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(raw_heap([]), [])

    def test_single_element_list(self):
        self.assertEqual(raw_heap([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(raw_heap([3, 1, 2]), [1, 2, 3])

    def test_negative_elements_list(self):
        self.assertEqual(raw_heap([-1, -2, -3]), [-3, -2, -1])

    def test_mixed_elements_list(self):
        self.assertEqual(raw_heap([3, -1, 2, 0]), [-1, 0, 2, 3])

    def test_duplicates_list(self):
        self.assertEqual(raw_heap([1, 2, 2, 3, 3, 3]), [1, 2, 2, 3, 3, 3])

    def test_large_list(self):
        self.assertEqual(raw_heap([i for i in range(100)]), list(range(100)))

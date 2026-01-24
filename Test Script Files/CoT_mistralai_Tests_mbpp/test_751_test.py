import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(check_min_heap([], 0))

    def test_single_element(self):
        for element in [1, -1]:
            self.assertTrue(check_min_heap([element], 0))

    def test_min_heap(self):
        arr = [1, 2, 3, 4, 5]
        for i in range(len(arr)):
            self.assertTrue(check_min_heap(arr, i))

    def test_invalid_index(self):
        arr = [1, 2, 3, 4, 5]
        with self.assertRaises(IndexError):
            check_min_heap(arr, len(arr))

    def test_non_heap_arrays(self):
        arr1 = [5, 3, 1, 4, 2]
        arr2 = [2, 1, 5, 4, 3]
        self.assertFalse(check_min_heap(arr1, 0))
        self.assertFalse(check_min_heap(arr2, 0))

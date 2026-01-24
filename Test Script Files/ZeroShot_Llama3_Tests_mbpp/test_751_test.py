import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):

    def test_valid_min_heap(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(check_min_heap(arr, 0))

    def test_invalid_min_heap(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertFalse(check_min_heap(arr, 0))

    def test_empty_array(self):
        arr = []
        self.assertFalse(check_min_heap(arr, 0))

    def test_single_element_array(self):
        arr = [1]
        self.assertTrue(check_min_heap(arr, 0))

    def test_two_element_array(self):
        arr = [1, 2]
        self.assertTrue(check_min_heap(arr, 0))

    def test_three_element_array(self):
        arr = [1, 2, 3]
        self.assertTrue(check_min_heap(arr, 0))

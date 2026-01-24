import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):
    def test_valid_min_heap(self):
        arr = [1, 2, 3, 4, 5]
        self.assertTrue(check_min_heap(arr, 0))

    def test_invalid_min_heap(self):
        arr = [5, 4, 3, 2, 1]
        self.assertFalse(check_min_heap(arr, 0))

    def test_edge_case_min_heap(self):
        arr = [1, 2, 3]
        self.assertTrue(check_min_heap(arr, 0))

    def test_empty_array_min_heap(self):
        arr = []
        self.assertTrue(check_min_heap(arr, 0))

    def test_single_element_array_min_heap(self):
        arr = [1]
        self.assertTrue(check_min_heap(arr, 0))

    def test_last_element_min_heap(self):
        arr = [1, 2, 3, 4, 5]
        self.assertTrue(check_min_heap(arr, 4))

    def test_non_integer_array_min_heap(self):
        arr = ['a', 'b', 'c', 'd', 'e']
        with self.assertRaises(TypeError):
            check_min_heap(arr, 0)

    def test_non_array_input_min_heap(self):
        with self.assertRaises(TypeError):
            check_min_heap(123, 0)

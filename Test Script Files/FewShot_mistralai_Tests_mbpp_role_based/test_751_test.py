import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(check_min_heap([]))

    def test_single_element(self):
        self.assertTrue(check_min_heap([1]))

    def test_min_heap_of_two_elements(self):
        self.assertTrue(check_min_heap([1, 2]))

    def test_min_heap_of_three_elements(self):
        self.assertTrue(check_min_heap([2, 1, 3]))

    def test_min_heap_of_four_elements(self):
        self.assertTrue(check_min_heap([1, 2, 3, 4]))

    def test_min_heap_with_duplicates(self):
        self.assertTrue(check_min_heap([1, 1, 2, 3]))

    def test_max_heap(self):
        self.assertFalse(check_min_heap([3, 2, 1]))

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            check_min_heap("not a list")

    def test_invalid_input_negative_index(self):
        with self.assertRaises(IndexError):
            check_min_heap([1, 2, 3], -1)

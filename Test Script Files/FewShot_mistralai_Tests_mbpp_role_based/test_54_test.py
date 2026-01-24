import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):
    def test_sorts_list_in_ascending_order(self):
        self.assertEqual(counting_sort([3, 1, 4, 1, 5, 9, 2, 6, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 6, 9])

    def test_handles_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_handles_single_element_list(self):
        self.assertEqual(counting_sort([0]), [0])

    def test_handles_negative_numbers(self):
        self.assertEqual(counting_sort([-1, -2, 0, 1, 2]), [-1, -2, 0, 1, 2])

    def test_handles_large_numbers(self):
        self.assertEqual(counting_sort([1000000, 999999, 999998, 1, 0]), [0, 1, 999998, 999999, 1000000])

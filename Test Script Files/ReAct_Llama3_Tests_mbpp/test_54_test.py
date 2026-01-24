import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(counting_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(counting_sort([5, 2, 8, 6, 1, 3, 4]), [1, 2, 3, 4, 5, 6, 8])

    def test_duplicates(self):
        self.assertEqual(counting_sort([1, 2, 2, 3, 3, 3, 4, 5, 5]), [1, 2, 2, 3, 3, 3, 4, 5, 5])

    def test_max_value_zero(self):
        self.assertEqual(counting_sort([0]), [0])

    def test_max_value_one(self):
        self.assertEqual(counting_sort([1]), [1])

    def test_max_value_large(self):
        self.assertEqual(counting_sort([10, 20, 30, 40, 50]), [10, 20, 30, 40, 50])

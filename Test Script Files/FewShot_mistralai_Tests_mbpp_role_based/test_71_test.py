import unittest
from mbpp_71_code import comb_sort

class TestCombSort(unittest.TestCase):
    def test_sorted_list(self):
        self.assertEqual(comb_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_reverse_list(self):
        self.assertEqual(comb_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(comb_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(comb_sort([1]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(comb_sort([1, 1, 2, 3]), [1, 1, 2, 3])

    def test_large_list(self):
        nums = [i for i in range(100)]
        sorted_nums = sorted(nums)
        self.assertEqual(comb_sort(nums), sorted_nums)

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4]
        sorted_nums = sorted(nums)
        self.assertEqual(comb_sort(nums), sorted_nums)

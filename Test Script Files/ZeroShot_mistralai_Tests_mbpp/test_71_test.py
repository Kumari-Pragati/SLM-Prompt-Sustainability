import unittest
from mbpp_71_code import comb_sort

class TestCombSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(comb_sort([]), [])

    def test_single_element(self):
        self.assertEqual(comb_sort([1]), [1])

    def test_simple_list(self):
        self.assertEqual(comb_sort([6, 3, 7, 1, 8, 4, 2]), [1, 2, 3, 4, 6, 7, 8])

    def test_reverse_list(self):
        self.assertEqual(comb_sort([8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_duplicates(self):
        self.assertEqual(comb_sort([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]), [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5])

    def test_large_list(self):
        nums = [i for i in range(100)]
        sorted_nums = sorted(nums)
        self.assertEqual(comb_sort(nums), sorted_nums)

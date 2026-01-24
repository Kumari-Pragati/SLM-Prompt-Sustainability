import unittest
from mbpp_71_code import comb_sort

class TestCombSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(comb_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(comb_sort([1]), [1])

    def test_duplicates(self):
        self.assertEqual(comb_sort([1, 1, 2, 3]), [1, 1, 2, 3])

    def test_ascending_order(self):
        self.assertEqual(comb_sort([1, 2, 3]), [1, 2, 3])

    def test_descending_order(self):
        self.assertEqual(comb_sort([3, 2, 1]), [1, 2, 3])

    def test_random_order(self):
        random_list = [5, 3, 8, 1, 6, 2, 9, 4, 7]
        sorted_list = sorted(random_list)
        self.assertEqual(comb_sort(random_list), sorted_list)

    def test_large_list(self):
        large_list = [i for i in range(100)]
        sorted_list = sorted(large_list)
        self.assertEqual(comb_sort(large_list), sorted_list)

    def test_negative_numbers(self):
        mixed_list = [-3, -2, -1, 0, 1, 2, 3]
        sorted_list = sorted(mixed_list)
        self.assertEqual(comb_sort(mixed_list), sorted_list)

    def test_shrink_factor_beyond_limit(self):
        with self.assertRaises(ValueError):
            def_shrink_factor = 1.4
            comb_sort_def_shrink_factor = lambda nums: comb_sort(nums, def_shrink_factor)
            comb_sort_def_shrink_factor([1, 2, 3])

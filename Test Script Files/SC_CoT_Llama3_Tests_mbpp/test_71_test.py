import unittest
from mbpp_71_code import comb_sort

class TestCombSort(unittest.TestCase):
    def test_typical_input(self):
        nums = [5, 2, 8, 6, 1, 9, 3, 7, 4]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(comb_sort(nums), expected)

    def test_edge_case_empty_list(self):
        nums = []
        expected = []
        self.assertEqual(comb_sort(nums), expected)

    def test_edge_case_single_element_list(self):
        nums = [5]
        expected = [5]
        self.assertEqual(comb_sort(nums), expected)

    def test_edge_case_sorted_list(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(comb_sort(nums), expected)

    def test_edge_case_reverse_sorted_list(self):
        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(comb_sort(nums), expected)

    def test_edge_case_duplicates(self):
        nums = [5, 2, 8, 6, 1, 9, 3, 7, 4, 5]
        expected = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
        self.assertEqual(comb_sort(nums), expected)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            comb_sort("not a list")

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            comb_sort([1, 2, "a", 4, 5])

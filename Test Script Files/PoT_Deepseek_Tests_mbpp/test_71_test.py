import unittest
from mbpp_71_code import comb_sort

class TestCombSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(comb_sort([5, 3, 2, 1, 4]), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(comb_sort([]), [])

    def test_single_element(self):
        self.assertEqual(comb_sort([1]), [1])

    def test_already_sorted(self):
        self.assertEqual(comb_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(comb_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(comb_sort([1, 2, 2, 3, 4]), [1, 2, 2, 3, 4])

    def test_negative_numbers(self):
        self.assertEqual(comb_sort([-5, -3, -2, -1, -4]), [-5, -4, -3, -2, -1])

    def test_large_numbers(self):
        self.assertEqual(comb_sort([100, 200, 300, 400, 500]), [100, 200, 300, 400, 500])

import unittest
from mbpp_141_code import pancake_sort

class TestPancakeSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(pancake_sort([3, 2, 4, 1]), [1, 3, 2, 4])
        self.assertEqual(pancake_sort([1, 1, 1, 1]), [1, 1, 1, 1])
        self.assertEqual(pancake_sort([5, 1, 9, 5, 5, 1]), [1, 5, 1, 9, 5, 5])

    def test_edge_case_single_element(self):
        self.assertEqual(pancake_sort([1]), [1])

    def test_edge_case_empty_list(self):
        self.assertEqual(pancake_sort([]), [])

    def test_edge_case_duplicate_max_at_start(self):
        self.assertEqual(pancake_sort([5, 5, 2, 1]), [1, 2, 5, 5])

    def test_edge_case_duplicate_max_at_end(self):
        self.assertEqual(pancake_sort([3, 2, 3]), [3, 2, 3])

    def test_corner_case_max_at_both_ends(self):
        self.assertEqual(pancake_sort([5, 3, 5]), [5, 3, 5])

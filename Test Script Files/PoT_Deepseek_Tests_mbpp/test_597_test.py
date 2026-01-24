import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_kth([1, 3, 5], [2, 4, 6], 3, 3, 3), 4)

    def test_edge_case_k_equals_1(self):
        self.assertEqual(find_kth([1, 3, 5], [2, 4, 6], 3, 3, 1), 1)

    def test_edge_case_k_equals_total_length(self):
        self.assertEqual(find_kth([1, 3, 5], [2, 4, 6], 3, 3, 6), 6)

    def test_edge_case_one_array_empty(self):
        self.assertEqual(find_kth([], [2, 4, 6], 0, 3, 3), 4)

    def test_edge_case_both_arrays_empty(self):
        self.assertIsNone(find_kth([], [], 0, 0, 1))

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(find_kth([1, 2, 3], [1, 2, 3], 3, 3, 3), 2)

    def test_corner_case_k_greater_than_total_length(self):
        with self.assertRaises(IndexError):
            find_kth([1, 3, 5], [2, 4, 6], 3, 3, 7)

import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDnf(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sort_by_dnf([], 0), [])

    def test_single_element_array(self):
        self.assertEqual(sort_by_dnf([1], 1), [1])

    def test_all_zeros_array(self):
        self.assertEqual(sort_by_dnf([0, 0, 0], 3), [0, 0, 0])

    def test_all_ones_array(self):
        self.assertEqual(sort_by_dnf([1, 1, 1], 3), [1, 1, 1])

    def test_mixed_array(self):
        self.assertEqual(sort_by_dnf([0, 1, 1, 0, 1], 5), [0, 0, 0, 1, 1])

    def test_edge_case_array(self):
        self.assertEqual(sort_by_dnf([0, 1, 0, 1, 0], 5), [0, 0, 0, 1, 1])

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            sort_by_dnf([1, 2, 3], -1)

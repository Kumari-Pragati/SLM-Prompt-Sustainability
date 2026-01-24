import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDnf(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sort_by_dnf([0, 1, 1, 0, 1, 0], 6), [0, 0, 0, 1, 1, 1])

    def test_edge_case_zero(self):
        self.assertEqual(sort_by_dnf([0, 1, 1, 0, 1, 0], 0), [])

    def test_edge_case_one(self):
        self.assertEqual(sort_by_dnf([1, 1, 1, 1, 1, 1], 6), [1, 1, 1, 1, 1, 1])

    def test_edge_case_empty(self):
        self.assertEqual(sort_by_dnf([], 0), [])

    def test_edge_case_single(self):
        self.assertEqual(sort_by_dnf([0], 1), [0])

    def test_edge_case_duplicates(self):
        self.assertEqual(sort_by_dnf([0, 0, 1, 1, 1, 0], 6), [0, 0, 0, 1, 1, 1])

    def test_edge_case_negative(self):
        with self.assertRaises(IndexError):
            sort_by_dnf([-1, 1, 1, 0, 1, 0], 6)

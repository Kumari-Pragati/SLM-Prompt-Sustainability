import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDnf(unittest.TestCase):

    def test_sort_by_dnf(self):
        self.assertEqual(sort_by_dnf([0, 1, 1, 0, 1, 0], 6), [0, 0, 0, 1, 1, 1])
        self.assertEqual(sort_by_dnf([1, 0, 1, 0, 1, 0], 6), [0, 0, 0, 1, 1, 1])
        self.assertEqual(sort_by_dnf([0, 0, 1, 1, 0, 1], 6), [0, 0, 0, 1, 1, 1])
        self.assertEqual(sort_by_dnf([1, 1, 1, 1, 1, 1], 6), [1, 1, 1, 1, 1, 1])
        self.assertEqual(sort_by_dnf([0, 0, 0, 0, 0, 0], 6), [0, 0, 0, 0, 0, 0])
        self.assertEqual(sort_by_dnf([1, 1, 1, 1, 1, 1], 6), [1, 1, 1, 1, 1, 1])
        self.assertEqual(sort_by_dnf([0, 1, 1, 1, 0, 1], 6), [0, 0, 0, 1, 1, 1])
        self.assertEqual(sort_by_dnf([1, 0, 1, 1, 0, 1], 6), [0, 0, 0, 1, 1, 1])
        self.assertEqual(sort_by_dnf([0, 0, 1, 1, 0, 1], 6), [0, 0, 0, 1, 1, 1])
        self.assertEqual(sort_by_dnf([1, 1, 1, 1, 1, 1], 6), [1, 1, 1, 1, 1, 1])
        self.assertEqual(sort_by_dnf([0, 0, 0, 0, 0, 0], 6), [0, 0, 0, 0, 0, 0])

    def test_sort_by_dnf_edge_cases(self):
        self.assertEqual(sort_by_dnf([], 0), [])
        self.assertEqual(sort_by_dnf([0], 1), [0])
        self.assertEqual(sort_by_dnf([1], 1), [1])
        self.assertEqual(sort_by_dnf([0, 1], 2), [0, 1])
        self.assertEqual(sort_by_dnf([1, 0], 2), [0, 1])

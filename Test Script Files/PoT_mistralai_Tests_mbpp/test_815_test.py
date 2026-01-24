import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDNF(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(sort_by_dnf([0, 1, 1, 0, 1, 0, 1], 7), [0, 0, 1, 1, 1, 1, 1])
        self.assertEqual(sort_by_dnf([1, 0, 1, 1, 0], 5), [0, 0, 1, 1, 1])
        self.assertEqual(sort_by_dnf([0, 0, 1, 1, 0, 1, 1], 7), [0, 0, 0, 1, 1, 1, 1])

    def test_edge_and_boundary_cases(self):
        self.assertEqual(sort_by_dnf([], 0), [])
        self.assertEqual(sort_by_dnf([0], 1), [0])
        self.assertEqual(sort_by_dnf([1], 1), [1])
        self.assertEqual(sort_by_dnf([0, 1], 2), [0, 1])
        self.assertEqual(sort_by_dnf([1, 0], 2), [1, 0])
        self.assertEqual(sort_by_dnf([0, 0, 1, 1], 4), [0, 0, 1, 1])
        self.assertEqual(sort_by_dnf([1, 1, 0, 0], 4), [0, 0, 1, 1])

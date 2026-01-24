import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDNF(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sort_by_dnf([0, 1, 1, 0, 1], 5), [0, 0, 1, 1, 1])
        self.assertEqual(sort_by_dnf([1, 0, 1, 0, 1], 5), [1, 1, 0, 0, 1])
        self.assertEqual(sort_by_dnf([0, 0, 1, 1, 1], 5), [0, 0, 1, 1, 1])

    def test_edge_and_boundary(self):
        self.assertEqual(sort_by_dnf([], 0), [])
        self.assertEqual(sort_by_dnf([0], 1), [0])
        self.assertEqual(sort_by_dnf([1], 0), [1])
        self.assertEqual(sort_by_dnf([0, 1], 2), [0, 1])
        self.assertEqual(sort_by_dnf([1, 0], 2), [1, 0])
        self.assertEqual(sort_by_dnf([0, 0, 0], 3), [0, 0, 0])
        self.assertEqual(sort_by_dnf([1, 1, 1], 3), [1, 1, 1])

    def test_complex(self):
        self.assertEqual(sort_by_dnf([0, 1, 0, 1, 0, 1], 6), [0, 0, 1, 1, 1, 1])
        self.assertEqual(sort_by_dnf([1, 0, 1, 0, 1, 0], 6), [1, 1, 0, 0, 0, 1])
        self.assertEqual(sort_by_dnf([0, 0, 1, 1, 0, 1], 6), [0, 0, 1, 1, 1, 1])
        self.assertEqual(sort_by_dnf([1, 1, 0, 0, 1, 1], 6), [1, 1, 1, 0, 0, 1])
        self.assertEqual(sort_by_dnf([0, 1, 1, 0, 1, 1], 6), [0, 0, 1, 1, 1, 1])

import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDnf(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sort_by_dnf([2, 1, 0, 2, 1, 0, 1, 2, 0], 9), [0, 0, 0, 1, 1, 1, 2, 2, 2])

    def test_edge_conditions(self):
        self.assertEqual(sort_by_dnf([], 0), [])
        self.assertEqual(sort_by_dnf([0], 1), [0])
        self.assertEqual(sort_by_dnf([1], 1), [1])
        self.assertEqual(sort_by_dnf([2], 1), [2])

    def test_complex_cases(self):
        self.assertEqual(sort_by_dnf([1, 0, 2, 1, 0, 2, 1, 0, 2], 9), [0, 0, 0, 1, 1, 1, 2, 2, 2])
        self.assertEqual(sort_by_dnf([2, 2, 2, 1, 1, 1, 0, 0, 0], 9), [0, 0, 0, 1, 1, 1, 2, 2, 2])
        self.assertEqual(sort_by_dnf([0, 1, 2, 0, 1, 2, 0, 1, 2], 9), [0, 0, 0, 1, 1, 1, 2, 2, 2])

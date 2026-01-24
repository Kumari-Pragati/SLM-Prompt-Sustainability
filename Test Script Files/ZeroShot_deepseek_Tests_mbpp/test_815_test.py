import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDnf(unittest.TestCase):

    def test_sort_by_dnf(self):
        self.assertEqual(sort_by_dnf([2, 1, 0, 2, 1, 0, 1, 2, 0, 1, 2, 0], 12), [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1, 2])
        self.assertEqual(sort_by_dnf([0, 1, 2, 0, 1, 2], 6), [0, 0, 1, 1, 2, 2])
        self.assertEqual(sort_by_dnf([1, 1, 1, 1, 1, 1], 6), [1, 1, 1, 1, 1, 1])
        self.assertEqual(sort_by_dnf([2, 2, 2, 2, 2, 2], 6), [2, 2, 2, 2, 2, 2])
        self.assertEqual(sort_by_dnf([], 0), [])

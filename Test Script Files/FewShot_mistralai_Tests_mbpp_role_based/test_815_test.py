import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDNF(unittest.TestCase):
    def test_sort_empty_list(self):
        self.assertEqual(sort_by_dnf([], 0), [])

    def test_sort_single_element_list(self):
        self.assertEqual(sort_by_dnf([0], 1), [0])
        self.assertEqual(sort_by_dnf([1], 1), [1])
        self.assertEqual(sort_by_dnf([2], 1), [2])

    def test_sort_two_elements_list(self):
        self.assertEqual(sort_by_dnf([0, 1], 2), [0, 1])
        self.assertEqual(sort_by_dnf([1, 0], 2), [0, 1])
        self.assertEqual(sort_by_dnf([2, 1], 2), [1, 2])
        self.assertEqual(sort_by_dnf([1, 2], 2), [1, 2])
        self.assertEqual(sort_by_dnf([2, 0], 2), [0, 2])

    def test_sort_multiple_elements_list(self):
        self.assertEqual(sort_by_dnf([0, 1, 2, 0, 1, 2], 6), [0, 0, 1, 1, 2, 2])
        self.assertEqual(sort_by_dnf([2, 0, 1, 2, 0, 1], 6), [0, 0, 1, 1, 2, 2])
        self.assertEqual(sort_by_dnf([1, 2, 0, 1, 2, 0], 6), [0, 0, 1, 1, 2, 2])

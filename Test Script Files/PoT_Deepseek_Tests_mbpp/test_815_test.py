import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDnf(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_by_dnf([2, 1, 0, 2, 1, 0, 1, 2, 0], 9), [0, 0, 0, 1, 1, 1, 2, 2, 2])

    def test_edge_case_empty_array(self):
        self.assertEqual(sort_by_dnf([], 0), [])

    def test_boundary_case_single_element(self):
        self.assertEqual(sort_by_dnf([0], 1), [0])
        self.assertEqual(sort_by_dnf([1], 1), [1])
        self.assertEqual(sort_by_dnf([2], 1), [2])

    def test_corner_case_all_elements_same(self):
        self.assertEqual(sort_by_dnf([0, 0, 0, 0, 0], 5), [0, 0, 0, 0, 0])
        self.assertEqual(sort_by_dnf([1, 1, 1, 1, 1], 5), [1, 1, 1, 1, 1])
        self.assertEqual(sort_by_dnf([2, 2, 2, 2, 2], 5), [2, 2, 2, 2, 2])

    def test_tricky_case_mixed_elements(self):
        self.assertEqual(sort_by_dnf([1, 2, 0, 2, 0, 1, 0, 2, 1], 9), [0, 0, 0, 1, 1, 1, 2, 2, 2])

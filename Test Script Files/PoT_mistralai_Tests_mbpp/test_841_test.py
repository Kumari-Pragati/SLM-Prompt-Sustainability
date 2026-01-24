import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_inv_count([1, 2, 4, 3], 4), 3)
        self.assertEqual(get_inv_count([5, 1, 9, 5, 5], 5), 4)
        self.assertEqual(get_inv_count([10, 20, 10], 3), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(get_inv_count([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(get_inv_count([1], 1), 0)

    def test_edge_case_duplicates(self):
        self.assertEqual(get_inv_count([1, 1, 2], 3), 1)

    def test_corner_case_reverse_order(self):
        self.assertEqual(get_inv_count([5, 4, 3, 2, 1], 5), 10)

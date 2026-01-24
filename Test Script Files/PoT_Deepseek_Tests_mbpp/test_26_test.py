import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6)], 3))

    def test_edge_case_K_in_list(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6)], 2))

    def test_edge_case_empty_list(self):
        self.assertTrue(check_k_elements([], 0))

    def test_boundary_case_K_at_boundary(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6)], 1))
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6)], 7))

    def test_corner_case_K_not_in_tuples(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6)], 8))

    def test_corner_case_K_in_multiple_tuples(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 9))

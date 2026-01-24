import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 1)], 2), [(5, 1), (3, 4)])

    def test_edge_case_k_equals_zero(self):
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 1)], 0), [])

    def test_edge_case_k_equals_length_of_list(self):
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 1)], 3), [(1, 2), (3, 4), (5, 1)])

    def test_boundary_case_k_greater_than_length_of_list(self):
        self.assertEqual(min_k([(1, 2), (3, 4), (5, 1)], 5), [(1, 2), (3, 4), (5, 1)])

    def test_corner_case_duplicate_second_elements(self):
        self.assertEqual(min_k([(1, 2), (3, 2), (5, 1)], 2), [(5, 1), (1, 2)])

    def test_corner_case_negative_second_elements(self):
        self.assertEqual(min_k([(1, -2), (3, -4), (5, -1)], 2), [(5, -1), (1, -2)])

    def test_corner_case_same_second_elements(self):
        self.assertEqual(min_k([(1, 2), (3, 2), (5, 2)], 2), [(5, 2), (1, 2)])

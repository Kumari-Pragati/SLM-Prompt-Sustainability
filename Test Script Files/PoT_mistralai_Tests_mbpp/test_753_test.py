import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_k([(1, 3), (2, 4), (3, 5), (4, 6), (5, 7)], 3), [((1, 3),), ((2, 4),), ((3, 5),)])

    def test_edge_case_empty_list(self):
        self.assertEqual(min_k([], 1), [])

    def test_edge_case_single_element(self):
        self.assertEqual(min_k([(1, 1)], 1), [((1, 1),)])

    def test_edge_case_single_element_k_greater_than_list_size(self):
        self.assertEqual(min_k([(1, 1)], 2), [((1, 1),)])

    def test_edge_case_single_element_negative_k(self):
        self.assertEqual(min_k([(1, 1)], -1), [])

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(min_k([(1, 1), (1, 1), (2, 2)], 2), [((1, 1),), ((2, 2),)])

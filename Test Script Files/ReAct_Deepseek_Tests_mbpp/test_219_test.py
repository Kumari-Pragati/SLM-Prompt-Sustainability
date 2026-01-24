import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 5))

    def test_boundary_case_K_equals_zero(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 0), ())

    def test_boundary_case_K_equals_one(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 1), (1, 5))

    def test_boundary_case_K_equals_len_of_tuple(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 5), (1, 5))

    def test_edge_case_K_greater_than_len_of_tuple(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 10), (1, 5))

    def test_edge_case_K_less_than_zero(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), -1), ())

    def test_edge_case_empty_tuple(self):
        self.assertEqual(extract_min_max((), 2), ())

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(extract_min_max((5,), 1), (5,))

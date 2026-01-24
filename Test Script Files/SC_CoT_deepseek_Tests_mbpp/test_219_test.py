import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 5))

    def test_edge_case_k_equals_one(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 1), (1, 5))

    def test_boundary_case_k_equals_zero(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 0), ())

    def test_edge_case_k_equals_length(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 5), (1, 2, 3, 4, 5))

    def test_corner_case_k_greater_than_length(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 6), (1, 5))

    def test_invalid_input_k_negative(self):
        with self.assertRaises(Exception):
            extract_min_max((1, 2, 3, 4, 5), -1)

    def test_invalid_input_k_float(self):
        with self.assertRaises(Exception):
            extract_min_max((1, 2, 3, 4, 5), 1.5)

    def test_invalid_input_k_string(self):
        with self.assertRaises(Exception):
            extract_min_max((1, 2, 3, 4, 5), '1')

    def test_invalid_input_tup_empty(self):
        self.assertEqual(extract_min_max((), 1), ())

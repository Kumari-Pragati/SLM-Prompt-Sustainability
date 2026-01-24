import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 5))

    def test_edge_case_K_equals_one(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 1), (1, 5))

    def test_boundary_case_K_equals_length_of_tup(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 5), (1, 5))

    def test_corner_case_K_greater_than_length_of_tup(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 6), (1, 5))

    def test_invalid_input_K_less_than_zero(self):
        with self.assertRaises(Exception):
            extract_min_max((1, 2, 3, 4, 5), -1)

    def test_invalid_input_empty_tup(self):
        self.assertEqual(extract_min_max((), 1), ())

    def test_typical_case_with_duplicate_values(self):
        self.assertEqual(extract_min_max((1, 2, 2, 3, 4, 5), 2), (1, 5))

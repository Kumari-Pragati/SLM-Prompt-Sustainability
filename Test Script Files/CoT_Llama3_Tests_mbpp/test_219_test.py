import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 5))

    def test_edge_case_K_0(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 0), ())

    def test_edge_case_K_equal_to_length(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 5), (1, 2, 3, 4, 5))

    def test_edge_case_K_greater_than_length(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 6), (1, 2, 3, 4, 5))

    def test_invalid_input_non_integer_K(self):
        with self.assertRaises(TypeError):
            extract_min_max((1, 2, 3, 4, 5), 'a')

    def test_invalid_input_non_tuple_input(self):
        with self.assertRaises(TypeError):
            extract_min_max(123, 2)

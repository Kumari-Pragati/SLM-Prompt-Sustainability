import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 5))

    def test_edge_case_K_zero(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 0), ())

    def test_edge_case_K_at_end(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 5), (1, 5))

    def test_edge_case_K_at_start(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 1), (1, 5))

    def test_edge_case_K_at_middle(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 3), (1, 4))

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            extract_min_max((1, 2, 3, 4, 5), 'a')

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            extract_min_max(123, 2)

import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):

    def test_simple_valid_input(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 5), 1)

    def test_edge_case_empty_array(self):
        self.assertEqual(get_pairs_count([], 0, 10), 0)

    def test_boundary_case_minimum_maximum_values(self):
        self.assertEqual(get_pairs_count([-1000, 1000], 2, 0), 1)
        self.assertEqual(get_pairs_count([-1000, 1000], 2, 2000), 1)

    def test_complex_case_duplicates(self):
        self.assertEqual(get_pairs_count([1, 2, 1, 2, 3, 4, 5], 7, 3), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_pairs_count("1, 2, 3, 4, 5", 5, 5)

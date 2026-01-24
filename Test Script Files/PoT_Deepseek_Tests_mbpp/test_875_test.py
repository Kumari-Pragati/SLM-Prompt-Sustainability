import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(min_difference([(1, 2), (3, 4)]), 1)

    def test_edge_case_single_pair(self):
        self.assertAlmostEqual(min_difference([(1, 1)]), 0)

    def test_boundary_case_negative_numbers(self):
        self.assertAlmostEqual(min_difference([(-1, 1), (2, 3)]), 1)

    def test_corner_case_large_numbers(self):
        self.assertAlmostEqual(min_difference([(1000000, 2000000), (3000000, 4000000)]), 1000000)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(TypeError):
            min_difference([])

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            min_difference([(1, 2), 3])

    def test_invalid_input_single_number(self):
        with self.assertRaises(TypeError):
            min_difference([1])

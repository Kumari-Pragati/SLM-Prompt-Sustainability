import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)

    def test_edge_case_same_length_arrays(self):
        self.assertAlmostEqual(get_median([1, 2, 3], [4, 5, 6], 3), 3.5)

    def test_edge_case_one_element_arrays(self):
        self.assertAlmostEqual(get_median([1], [2], 1), 1.5)

    def test_boundary_case_empty_arrays(self):
        self.assertAlmostEqual(get_median([], [], 0), 0)

    def test_invalid_input_negative_numbers(self):
        with self.assertRaises(Exception):
            get_median([-1, -2, -3], [1, 2, 3], 3)

    def test_invalid_input_non_integer_arrays(self):
        with self.assertRaises(Exception):
            get_median(['1', '2', '3'], [4, 5, 6], 3)

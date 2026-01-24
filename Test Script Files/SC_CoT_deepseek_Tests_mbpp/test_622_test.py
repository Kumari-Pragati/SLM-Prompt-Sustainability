import unittest

from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)

    def test_edge_case_with_equal_length_arrays(self):
        self.assertAlmostEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)

    def test_edge_case_with_one_element_arrays(self):
        self.assertAlmostEqual(get_median([1], [2], 1), 1.5)

    def test_edge_case_with_empty_arrays(self):
        self.assertEqual(get_median([], [], 0), None)

    def test_invalid_input_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            get_median([1, 3, '5'], [2, 4, 6], 3)

    def test_invalid_input_with_negative_elements(self):
        with self.assertRaises(ValueError):
            get_median([1, 3, -5], [2, 4, 6], 3)

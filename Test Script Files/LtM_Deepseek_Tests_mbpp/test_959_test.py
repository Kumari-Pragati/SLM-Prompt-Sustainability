import unittest
from mbpp_959_code import Average

class TestAverage(unittest.TestCase):
    def test_simple_average(self):
        self.assertAlmostEqual(Average([1, 2, 3, 4, 5]), 3.0)

    def test_edge_case_empty_list(self):
        self.assertEqual(Average([]), 0)

    def test_boundary_case_single_element(self):
        self.assertEqual(Average([1]), 1)

    def test_edge_case_negative_numbers(self):
        self.assertAlmostEqual(Average([-1, -2, -3, -4, -5]), -3.0)

    def test_boundary_case_max_and_min_values(self):
        self.assertEqual(Average([float('inf'), float('-inf')]), float('nan'))

    def test_complex_case_mixed_positive_negative(self):
        self.assertAlmostEqual(Average([-1, 1, -2, 2, -3, 3]), 0.0)

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            Average(['a', 'b', 'c'])

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(TypeError):
            Average([1, 'two', 3])

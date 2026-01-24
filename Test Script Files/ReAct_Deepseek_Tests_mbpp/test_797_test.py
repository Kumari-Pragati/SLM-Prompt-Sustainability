import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_in_Range(1, 10), 26)

    def test_boundary_case_lower(self):
        self.assertEqual(sum_in_Range(1, 1), 1)

    def test_boundary_case_upper(self):
        self.assertEqual(sum_in_Range(10, 100), 2644)

    def test_edge_case_lower_zero(self):
        self.assertEqual(sum_in_Range(0, 10), 26)

    def test_edge_case_upper_zero(self):
        self.assertEqual(sum_in_Range(10, 0), 0)

    def test_edge_case_negative_range(self):
        self.assertEqual(sum_in_Range(-10, 10), 0)

    def test_edge_case_identical_numbers(self):
        self.assertEqual(sum_in_Range(5, 5), 1)

    def test_error_case_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_in_Range("1", 10)

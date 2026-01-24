import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)

    def test_edge_case_with_equal_numbers(self):
        self.assertEqual(median_numbers(1, 1, 1), 1)

    def test_boundary_case_with_smallest_number(self):
        self.assertEqual(median_numbers(0, 1, 2), 1)

    def test_boundary_case_with_largest_number(self):
        self.assertEqual(median_numbers(2, 3, 4), 3)

    def test_corner_case_with_equal_numbers_and_boundary(self):
        self.assertEqual(median_numbers(0, 0, 0), 0)

    def test_corner_case_with_smallest_and_largest_numbers(self):
        self.assertEqual(median_numbers(0, 1, 0), 0)

    def test_corner_case_with_largest_and_smallest_numbers(self):
        self.assertEqual(median_numbers(2, 1, 2), 2)

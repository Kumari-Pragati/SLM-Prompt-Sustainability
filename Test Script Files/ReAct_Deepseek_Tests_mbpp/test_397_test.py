import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)

    def test_edge_case_with_equal_numbers(self):
        self.assertEqual(median_numbers(2, 2, 2), 2)

    def test_edge_case_with_two_equal_numbers(self):
        self.assertEqual(median_numbers(1, 2, 1), 1)

    def test_edge_case_with_three_equal_numbers(self):
        self.assertEqual(median_numbers(2, 2, 2), 2)

    def test_edge_case_with_max_number_first(self):
        self.assertEqual(median_numbers(5, 3, 2), 3)

    def test_edge_case_with_max_number_last(self):
        self.assertEqual(median_numbers(1, 2, 5), 2)

    def test_edge_case_with_min_number_first(self):
        self.assertEqual(median_numbers(-1, -2, -3), -2)

    def test_edge_case_with_min_number_last(self):
        self.assertEqual(median_numbers(3, 2, -1), 2)

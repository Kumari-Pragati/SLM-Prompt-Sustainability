import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(median_numbers(5, 3, 2), 3)

    def test_edge_case_a_greater_than_b_and_c(self):
        self.assertEqual(median_numbers(5, 2, 3), 3)

    def test_edge_case_b_greater_than_a_and_c(self):
        self.assertEqual(median_numbers(2, 5, 3), 3)

    def test_edge_case_c_greater_than_a_and_b(self):
        self.assertEqual(median_numbers(2, 3, 5), 3)

    def test_edge_case_a_equal_to_b_and_c(self):
        self.assertEqual(median_numbers(3, 3, 3), 3)

    def test_edge_case_b_equal_to_a_and_c(self):
        self.assertEqual(median_numbers(3, 3, 3), 3)

    def test_edge_case_c_equal_to_a_and_b(self):
        self.assertEqual(median_numbers(3, 3, 3), 3)

    def test_edge_case_a_greater_than_b_and_a_greater_than_c(self):
        self.assertEqual(median_numbers(5, 3, 2), 3)

    def test_edge_case_b_greater_than_a_and_b_greater_than_c(self):
        self.assertEqual(median_numbers(2, 5, 3), 3)

    def test_edge_case_c_greater_than_a_and_b_greater_than_c(self):
        self.assertEqual(median_numbers(2, 3, 5), 3)

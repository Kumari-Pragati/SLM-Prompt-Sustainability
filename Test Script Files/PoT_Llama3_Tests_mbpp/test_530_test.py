import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(negative_count([-1, 2, 3, -4, 5]), 0.4)

    def test_edge_case_zero(self):
        self.assertEqual(negative_count([0, 0, 0]), 0.0)

    def test_edge_case_all_negative(self):
        self.assertEqual(negative_count([-1, -2, -3, -4, -5]), 1.0)

    def test_edge_case_all_positive(self):
        self.assertEqual(negative_count([1, 2, 3, 4, 5]), 0.0)

    def test_edge_case_mixed(self):
        self.assertEqual(negative_count([-1, 2, 3, -4, 5]), 0.4)

    def test_edge_case_single_negative(self):
        self.assertEqual(negative_count([-1, 1, 2, 3, 4]), 0.2)

    def test_edge_case_single_positive(self):
        self.assertEqual(negative_count([1, 2, 3, 4, 5]), 0.0)

    def test_edge_case_no_numbers(self):
        self.assertEqual(negative_count([]), 0.0)

    def test_edge_case_single_zero(self):
        self.assertEqual(negative_count([0]), 0.0)

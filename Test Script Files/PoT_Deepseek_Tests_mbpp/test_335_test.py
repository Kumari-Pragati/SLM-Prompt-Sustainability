import unittest
from mbpp_335_code import ap_sum

class TestArithmeticProgressionSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(ap_sum(1, 5, 2), 14)

    def test_edge_case_single_term(self):
        self.assertEqual(ap_sum(1, 1, 2), 1)

    def test_boundary_case_zero_difference(self):
        self.assertEqual(ap_sum(1, 5, 0), 5)

    def test_corner_case_negative_difference(self):
        self.assertEqual(ap_sum(1, 5, -2), 0)

    def test_invalid_input_negative_terms(self):
        with self.assertRaises(Exception):
            ap_sum(-1, 5, 2)

    def test_invalid_input_negative_difference(self):
        with self.assertRaises(Exception):
            ap_sum(1, 5, -2)

    def test_invalid_input_zero_terms(self):
        with self.assertRaises(Exception):
            ap_sum(1, 0, 2)

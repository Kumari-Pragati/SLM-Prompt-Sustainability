import unittest
from mbpp_491_code import sum_gp

class TestSumGP(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sum_gp(2, 3, 0.5), 5.0)

    def test_edge_case_r_equals_1(self):
        self.assertEqual(sum_gp(2, 3, 1), 0.0)

    def test_boundary_case_n_equals_0(self):
        self.assertEqual(sum_gp(2, 0, 0.5), 0.0)

    def test_corner_case_r_greater_than_1(self):
        self.assertEqual(sum_gp(2, 3, 1.5), 0.0)

    def test_invalid_input_n_negative(self):
        with self.assertRaises(Exception):
            sum_gp(2, -3, 0.5)

    def test_invalid_input_r_not_a_number(self):
        with self.assertRaises(Exception):
            sum_gp(2, 3, 'a')

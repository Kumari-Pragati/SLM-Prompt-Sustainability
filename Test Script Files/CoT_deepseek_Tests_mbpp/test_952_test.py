import unittest
from mbpp_952_code import nCr_mod_p

class TestNCRModP(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(nCr_mod_p(5, 2, 13), 6)

    def test_edge_case_r_equals_n(self):
        self.assertEqual(nCr_mod_p(5, 5, 13), 1)

    def test_edge_case_r_equals_zero(self):
        self.assertEqual(nCr_mod_p(5, 0, 13), 1)

    def test_edge_case_r_greater_than_n(self):
        self.assertEqual(nCr_mod_p(5, 6, 13), 0)

    def test_invalid_input_negative_n(self):
        with self.assertRaises(Exception):
            nCr_mod_p(-5, 2, 13)

    def test_invalid_input_negative_r(self):
        with self.assertRaises(Exception):
            nCr_mod_p(5, -2, 13)

    def test_invalid_input_negative_p(self):
        with self.assertRaises(Exception):
            nCr_mod_p(5, 2, -13)

    def test_invalid_input_zero_p(self):
        with self.assertRaises(Exception):
            nCr_mod_p(5, 2, 0)

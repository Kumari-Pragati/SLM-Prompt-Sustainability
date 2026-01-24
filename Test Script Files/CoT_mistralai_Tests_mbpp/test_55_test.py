import unittest
from mbpp_55_code import tn_gp

class TestTnGp(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tn_gp(2, 3, 2), 8)

    def test_edge_case_zero_n(self):
        self.assertEqual(tn_gp(3, 0, 2), 0)

    def test_edge_case_one_n(self):
        self.assertEqual(tn_gp(4, 1, 3), 4)

    def test_edge_case_negative_n(self):
        self.assertEqual(tn_gp(5, -2, 2), 0)

    def test_edge_case_zero_r(self):
        self.assertEqual(tn_gp(6, 3, 0), 0)

    def test_edge_case_negative_r(self):
        self.assertEqual(tn_gp(7, 3, -2), 0)

    def test_invalid_input_negative_a(self):
        self.assertRaises(ValueError, tn_gp, -1, 3, 2)

    def test_invalid_input_zero_a(self):
        self.assertRaises(ValueError, tn_gp, 0, 3, 2)

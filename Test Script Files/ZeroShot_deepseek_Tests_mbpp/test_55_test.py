import unittest
from mbpp_55_code import tn_gp

class TestTN_GP(unittest.TestCase):

    def test_tn_gp_positive_numbers(self):
        self.assertEqual(tn_gp(2, 3, 2), 4)

    def test_tn_gp_negative_numbers(self):
        self.assertEqual(tn_gp(-2, 3, 2), -4)

    def test_tn_gp_zero_r(self):
        self.assertEqual(tn_gp(2, 3, 0), 0)

    def test_tn_gp_zero_a(self):
        self.assertEqual(tn_gp(0, 3, 2), 0)

    def test_tn_gp_zero_n(self):
        self.assertEqual(tn_gp(2, 0, 2), 0)

    def test_tn_gp_negative_n(self):
        self.assertEqual(tn_gp(2, -3, 2), 0)

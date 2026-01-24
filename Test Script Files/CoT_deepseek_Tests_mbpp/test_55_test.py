import unittest
from mbpp_55_code import tn_gp

class TestTN_GP(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(tn_gp(2, 3, 2), 4.0)

    def test_zero_r(self):
        self.assertEqual(tn_gp(2, 3, 0), 0)

    def test_negative_r(self):
        self.assertAlmostEqual(tn_gp(2, 3, -2), -4.0)

    def test_zero_n(self):
        self.assertEqual(tn_gp(2, 0, 2), 0)

    def test_negative_n(self):
        self.assertRaises(ValueError, tn_gp, 2, -3, 2)

    def test_zero_a(self):
        self.assertEqual(tn_gp(0, 3, 2), 0)

    def test_negative_a(self):
        self.assertAlmostEqual(tn_gp(-2, 3, 2), -4.0)

    def test_large_n(self):
        self.assertAlmostEqual(tn_gp(2, 1000, 2), 2**999)

    def test_large_r(self):
        self.assertAlmostEqual(tn_gp(2, 3, 1000), 2**2)

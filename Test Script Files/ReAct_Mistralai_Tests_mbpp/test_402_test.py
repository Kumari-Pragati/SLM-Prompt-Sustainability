import unittest
from mbpp_402_code import ncr_modp

class TestNCRModP(unittest.TestCase):

    def test_ncr_modp_basic(self):
        self.assertEqual(ncr_modp(2, 1, 3), 1)
        self.assertEqual(ncr_modp(3, 2, 5), 2)
        self.assertEqual(ncr_modp(5, 3, 7), 5)
        self.assertEqual(ncr_modp(10, 5, 11), 1)

    def test_ncr_modp_zero_r(self):
        self.assertEqual(ncr_modp(3, 0, 5), 1)

    def test_ncr_modp_negative_r(self):
        self.assertRaises(ValueError, ncr_modp, 3, -1, 5)

    def test_ncr_modp_negative_n(self):
        self.assertRaises(ValueError, ncr_modp, -3, 2, 5)

    def test_ncr_modp_zero_n(self):
        self.assertEqual(ncr_modp(0, 1, 3), 0)

    def test_ncr_modp_large_input(self):
        self.assertEqual(ncr_modp(1000, 500, 1009), 994)

    def test_ncr_modp_large_r(self):
        self.assertEqual(ncr_modp(10, 100, 1009), 1)

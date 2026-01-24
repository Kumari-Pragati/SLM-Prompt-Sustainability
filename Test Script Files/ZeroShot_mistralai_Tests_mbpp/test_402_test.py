import unittest
from mbpp_402_code import ncr_modp

class TestNCRModP(unittest.TestCase):

    def test_ncr_modp_basic(self):
        self.assertEqual(ncr_modp(4, 2, 3), 2)
        self.assertEqual(ncr_modp(5, 2, 5), 2)
        self.assertEqual(ncr_modp(5, 3, 5), 3)
        self.assertEqual(ncr_modp(6, 3, 7), 5)
        self.assertEqual(ncr_modp(7, 4, 11), 8)

    def test_ncr_modp_edge_cases(self):
        self.assertEqual(ncr_modp(0, 0, 2), 1)
        self.assertEqual(ncr_modp(0, 1, 2), 0)
        self.assertEqual(ncr_modp(1, 0, 2), 1)
        self.assertEqual(ncr_modp(1, 1, 2), 1)

    def test_ncr_modp_negative_arguments(self):
        self.assertRaises(ValueError, ncr_modp, -1, 2, 3)
        self.assertRaises(ValueError, ncr_modp, 1, -1, 3)
        self.assertRaises(ValueError, ncr_modp, 1, 2, -1)

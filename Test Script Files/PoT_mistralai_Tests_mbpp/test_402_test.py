import unittest
from mbpp_402_code import ncr_modp

class TestNCRModP(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(ncr_modp(5, 2, 3), 2)
        self.assertEqual(ncr_modp(10, 3, 5), 2)
        self.assertEqual(ncr_modp(20, 10, 11), 1)

    def test_edge_cases(self):
        self.assertEqual(ncr_modp(0, 0, 2), 1)
        self.assertEqual(ncr_modp(1, 0, 2), 1)
        self.assertEqual(ncr_modp(1, 1, 2), 1)
        self.assertEqual(ncr_modp(2, 2, 2), 0)

    def test_boundary_cases(self):
        self.assertEqual(ncr_modp(1, 1, 1), 1)
        self.assertEqual(ncr_modp(2, 2, 2), 0)
        self.assertEqual(ncr_modp(3, 3, 3), 1)

import unittest
from mbpp_402_code import ncr_modp

class TestNCRModP(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(ncr_modp(5, 3, 7), 4)
        self.assertEqual(ncr_modp(10, 4, 11), 5)
        self.assertEqual(ncr_modp(20, 10, 13), 6)

    def test_edge_cases(self):
        self.assertEqual(ncr_modp(0, 0, 5), 1)
        self.assertEqual(ncr_modp(1, 0, 5), 1)
        self.assertEqual(ncr_modp(1, 1, 5), 1)
        self.assertEqual(ncr_modp(1, 2, 5), 2)
        self.assertEqual(ncr_modp(2, 2, 5), 2)
        self.assertEqual(ncr_modp(3, 3, 5), 3)

    def test_boundary_conditions(self):
        self.assertEqual(ncr_modp(1, 0, 1), 1)
        self.assertEqual(ncr_modp(1, 1, 0), TraceError)
        self.assertEqual(ncr_modp(0, 1, 1), 0)
        self.assertEqual(ncr_modp(1, 1, 2), 1)
        self.assertEqual(ncr_modp(1, 2, 1), 0)

    def test_negative_inputs(self):
        self.assertRaises(ValueError, ncr_modp, -1, 2, 5)
        self.assertRaises(ValueError, ncr_modp, 2, -1, 5)
        self.assertRaises(ValueError, ncr_modp, 0, -1, 5)
        self.assertRaises(ValueError, ncr_modp, 2, 0, -5)

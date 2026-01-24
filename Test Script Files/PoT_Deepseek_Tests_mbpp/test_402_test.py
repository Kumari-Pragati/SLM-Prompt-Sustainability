import unittest
from mbpp_402_code import ncr_modp

class TestNcrModp(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(ncr_modp(5, 2, 13), 10)
        self.assertEqual(ncr_modp(10, 5, 23), 10)
        self.assertEqual(ncr_modp(15, 10, 31), 24)

    def test_edge_cases(self):
        self.assertEqual(ncr_modp(0, 0, 13), 1)
        self.assertEqual(ncr_modp(0, 1, 13), 0)
        self.assertEqual(ncr_modp(1, 0, 13), 1)

    def test_boundary_cases(self):
        self.assertEqual(ncr_modp(100, 50, 101), 0)
        self.assertEqual(ncr_modp(100, 100, 201), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            ncr_modp(-1, 2, 13)
        with self.assertRaises(Exception):
            ncr_modp(10, -1, 13)
        with self.assertRaises(Exception):
            ncr_modp(10, 20, 13)

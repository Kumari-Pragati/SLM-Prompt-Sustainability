import unittest
from mbpp_402_code import ncr_modp

class TestNcrModp(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(ncr_modp(5, 2, 13), 10)

    def test_boundary_case(self):
        self.assertEqual(ncr_modp(0, 0, 13), 1)
        self.assertEqual(ncr_modp(5, 5, 13), 1)

    def test_edge_case(self):
        self.assertEqual(ncr_modp(10, 0, 13), 1)
        self.assertEqual(ncr_modp(10, 10, 13), 1)

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            ncr_modp(-1, 2, 13)
        with self.assertRaises(Exception):
            ncr_modp(5, -1, 13)
        with self.assertRaises(Exception):
            ncr_modp(5, 6, 13)

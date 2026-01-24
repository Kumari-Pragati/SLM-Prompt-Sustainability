import unittest
from mbpp_402_code import ncr_modp

class TestNcrModp(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(ncr_modp(5, 2, 13), 10)

    def test_boundary_conditions(self):
        self.assertEqual(ncr_modp(0, 0, 13), 1)
        self.assertEqual(ncr_modp(10, 10, 13), 1)

    def test_edge_cases(self):
        self.assertEqual(ncr_modp(5, 0, 13), 1)
        self.assertEqual(ncr_modp(5, 5, 13), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            ncr_modp(-1, 2, 13)
        with self.assertRaises(ValueError):
            ncr_modp(5, -1, 13)
        with self.assertRaises(ValueError):
            ncr_modp(5, 6, 13)

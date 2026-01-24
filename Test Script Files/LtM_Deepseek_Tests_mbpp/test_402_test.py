import unittest
from mbpp_402_code import ncr_modp

class TestNcrModp(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(ncr_modp(5, 2, 13), 10)
        self.assertEqual(ncr_modp(10, 5, 23), 10)

    def test_edge_conditions(self):
        self.assertEqual(ncr_modp(0, 0, 13), 1)
        self.assertEqual(ncr_modp(5, 0, 13), 1)
        self.assertEqual(ncr_modp(5, 5, 13), 0)

    def test_boundary_conditions(self):
        self.assertEqual(ncr_modp(100, 50, 1000000007), 161700)
        self.assertEqual(ncr_modp(1000, 500, 1000000007), 0)

    def test_complex_cases(self):
        self.assertEqual(ncr_modp(1000, 500, 1000000007), 0)
        self.assertEqual(ncr_modp(1000, 999, 1000000007), 0)

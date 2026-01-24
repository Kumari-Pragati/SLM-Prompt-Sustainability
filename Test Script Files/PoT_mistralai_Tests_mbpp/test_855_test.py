import unittest
from mbpp_855_code import check_Even_Parity

class TestCheckEvenParity(unittest.TestCase):
    def test_typical_even(self):
        self.assertTrue(check_Even_Parity(10))

    def test_typical_odd(self):
        self.assertFalse(check_Even_Parity(15))

    def test_edge_zero(self):
        self.assertFalse(check_Even_Parity(0))

    def test_boundary_min_positive(self):
        self.assertTrue(check_Even_Parity(1))

    def test_boundary_max_positive(self.assertFalse(check_Even_Parity(2**31 - 1)))

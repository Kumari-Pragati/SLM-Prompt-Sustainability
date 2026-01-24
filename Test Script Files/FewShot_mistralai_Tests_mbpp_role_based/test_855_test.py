import unittest
from mbpp_855_code import check_Even_Parity

class TestCheckEvenParity(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(check_Even_Parity(4))

    def test_odd_number(self):
        self.assertFalse(check_Even_Parity(5))

    def test_zero(self):
        self.assertTrue(check_Even_Parity(0))

    def test_negative_number(self):
        self.assertTrue(check_Even_Parity(-4))

    def test_large_positive_number(self):
        self.assertTrue(check_Even_Parity(1000000))

    def test_large_negative_number(self):
        self.assertTrue(check_Even_Parity(-1000000))

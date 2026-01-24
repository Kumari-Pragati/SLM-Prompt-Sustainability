import unittest
from mbpp_855_code import check_Even_Parity

class TestCheckEvenParity(unittest.TestCase):

    def test_even_numbers(self):
        self.assertTrue(check_Even_Parity(2))
        self.assertTrue(check_Even_Parity(4))
        self.assertTrue(check_Even_Parity(6))
        self.assertTrue(check_Even_Parity(8))
        self.assertTrue(check_Even_Parity(10))

    def test_odd_numbers(self):
        self.assertFalse(check_Even_Parity(1))
        self.assertFalse(check_Even_Parity(3))
        self.assertFalse(check_Even_Parity(5))
        self.assertFalse(check_Even_Parity(7))
        self.assertFalse(check_Even_Parity(9))

    def test_zero(self):
        self.assertTrue(check_Even_Parity(0))

    def test_negative_numbers(self):
        self.assertTrue(check_Even_Parity(-2))
        self.assertTrue(check_Even_Parity(-4))
        self.assertFalse(check_Even_Parity(-1))
        self.assertTrue(check_Even_Parity(-3))

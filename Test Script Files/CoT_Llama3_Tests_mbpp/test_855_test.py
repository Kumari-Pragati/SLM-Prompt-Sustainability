import unittest
from mbpp_855_code import check_Even_Parity

class TestCheckEvenParity(unittest.TestCase):

    def test_even_parity(self):
        self.assertTrue(check_Even_Parity(10))
        self.assertTrue(check_Even_Parity(20))
        self.assertTrue(check_Even_Parity(30))

    def test_odd_parity(self):
        self.assertFalse(check_Even_Parity(9))
        self.assertFalse(check_Even_Parity(17))
        self.assertFalse(check_Even_Parity(25))

    def test_zero(self):
        self.assertTrue(check_Even_Parity(0))

    def test_negative(self):
        self.assertTrue(check_Even_Parity(-10))
        self.assertTrue(check_Even_Parity(-20))
        self.assertTrue(check_Even_Parity(-30))

    def test_non_integer(self):
        self.assertTrue(check_Even_Parity(10.5))
        self.assertTrue(check_Even_Parity(-10.5))

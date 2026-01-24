import unittest
from mbpp_855_code import check_Even_Parity

class TestCheckEvenParity(unittest.TestCase):

    def test_even_parity(self):
        self.assertTrue(check_Even_Parity(10))
        self.assertTrue(check_Even_Parity(14))
        self.assertTrue(check_Even_Parity(18))
        self.assertTrue(check_Even_Parity(22))

    def test_odd_parity(self):
        self.assertFalse(check_Even_Parity(11))
        self.assertFalse(check_Even_Parity(15))
        self.assertFalse(check_Even_Parity(19))
        self.assertFalse(check_Even_Parity(23))

    def test_zero(self):
        self.assertTrue(check_Even_Parity(0))

    def test_negative_numbers(self):
        self.assertTrue(check_Even_Parity(-10))
        self.assertTrue(check_Even_Parity(-14))
        self.assertTrue(check_Even_Parity(-18))
        self.assertTrue(check_Even_Parity(-22))

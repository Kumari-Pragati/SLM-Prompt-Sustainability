import unittest
from mbpp_768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):

    def test_positive_odd_parity(self):
        self.assertTrue(check_Odd_Parity(7))
        self.assertTrue(check_Odd_Parity(9))
        self.assertTrue(check_Odd_Parity(43))

    def test_positive_even_parity(self):
        self.assertFalse(check_Odd_Parity(8))
        self.assertFalse(check_Odd_Parity(10))
        self.assertFalse(check_Odd_Parity(44))

    def test_zero(self):
        self.assertFalse(check_Odd_Parity(0))

    def test_negative_numbers(self):
        self.assertFalse(check_Odd_Parity(-7))
        self.assertFalse(check_Odd_Parity(-9))
        self.assertFalse(check_Odd_Parity(-43))

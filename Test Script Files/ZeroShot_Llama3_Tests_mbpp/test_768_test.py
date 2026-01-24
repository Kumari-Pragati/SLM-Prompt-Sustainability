import unittest
from mbpp_768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):

    def test_even_number(self):
        self.assertFalse(check_Odd_Parity(10))

    def test_odd_number(self):
        self.assertTrue(check_Odd_Parity(9))

    def test_zero(self):
        self.assertFalse(check_Odd_Parity(0))

    def test_negative_number(self):
        self.assertTrue(check_Odd_Parity(-9))

    def test_large_number(self):
        self.assertTrue(check_Odd_Parity(1000003))

    def test_small_number(self):
        self.assertTrue(check_Odd_Parity(3))

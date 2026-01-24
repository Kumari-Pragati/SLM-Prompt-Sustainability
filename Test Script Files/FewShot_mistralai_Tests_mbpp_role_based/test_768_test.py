import unittest
from mbpp_768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):
    def test_odd_number(self):
        self.assertTrue(check_Odd_Parity(5))

    def test_even_number(self):
        self.assertFalse(check_Odd_Parity(4))

    def test_zero(self):
        self.assertFalse(check_Odd_Parity(0))

    def test_negative_number(self):
        self.assertFalse(check_Odd_Parity(-1))

    def test_max_int(self):
        self.assertTrue(check_Odd_Parity(2 ** 31 - 1))

    def test_min_int(self):
        self.assertFalse(check_Odd_Parity(-2 ** 31))

import unittest
from768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):
    def test_positive_odd_numbers(self):
        self.assertTrue(check_Odd_Parity(1))
        self.assertTrue(check_Odd_Parity(3))
        self.assertTrue(check_Odd_Parity(5))
        self.assertTrue(check_Odd_Parity(7))

    def test_positive_even_numbers(self):
        self.assertFalse(check_Odd_Parity(0))
        self.assertFalse(check_Odd_Parity(2))
        self.assertFalse(check_Odd_Parity(4))
        self.assertFalse(check_Odd_Parity(6))

    def test_zero(self):
        self.assertFalse(check_Odd_Parity(0))

    def test_negative_numbers(self):
        self.assertTrue(check_Odd_Parity(-1))
        self.assertTrue(check_Odd_Parity(-3))
        self.assertTrue(check_Odd_Parity(-5))
        self.assertTrue(check_Odd_Parity(-7))

    def test_large_numbers(self):
        self.assertTrue(check_Odd_Parity(2 ** 16 - 1))
        self.assertTrue(check_Odd_Parity(2 ** 32 - 1))
        self.assertTrue(check_Odd_Parity(2 ** 64 - 1))

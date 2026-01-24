import unittest
from mbpp_768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):
    def test_even_numbers(self):
        self.assertFalse(check_Odd_Parity(4))
        self.assertFalse(check_Odd_Parity(10))
        self.assertFalse(check_Odd_Parity(20))

    def test_odd_numbers(self):
        self.assertTrue(check_Odd_Parity(3))
        self.assertTrue(check_Odd_Parity(9))
        self.assertTrue(check_Odd_Parity(21))

    def test_zero(self):
        self.assertFalse(check_Odd_Parity(0))

    def test_negative_numbers(self):
        self.assertFalse(check_Odd_Parity(-4))
        self.assertFalse(check_Odd_Parity(-10))
        self.assertFalse(check_Odd_Parity(-20))

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            check_Odd_Parity(3.5)

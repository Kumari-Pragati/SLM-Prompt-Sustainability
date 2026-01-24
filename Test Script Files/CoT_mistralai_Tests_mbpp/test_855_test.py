import unittest
from mbpp_855_code import check_Even_Parity

class TestCheckEvenParity(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(check_Even_Parity(10))

    def test_odd_number(self):
        self.assertFalse(check_Even_Parity(7))

    def test_zero(self):
        self.assertTrue(check_Even_Parity(0))

    def test_negative_number(self):
        self.assertTrue(check_Even_Parity(-10))

    def test_large_positive_number(self):
        self.assertTrue(check_Even_Parity(2 ** 31 - 1))

    def test_large_negative_number(self):
        self.assertTrue(check_Even_Parity(-2 ** 31 + 1))

    def test_float(self):
        self.assertFalse(check_Even_Parity(3.14))

    def test_string(self):
        self.assertRaises(TypeError, check_Even_Parity, "abc")
